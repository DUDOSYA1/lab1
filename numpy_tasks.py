"""Заготовки задач на NumPy."""

import matplotlib.pyplot as plt
import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def notPassedTest(functionOutput, expectedOutput) -> bool:
    if isinstance(functionOutput, list) and isinstance(expectedOutput, list):
        return functionOutput != expectedOutput

    functionOutput = np.asarray(functionOutput)
    expectedOutput = np.asarray(expectedOutput)

    if functionOutput.shape != expectedOutput.shape:
        return True
    if np.allclose(functionOutput, expectedOutput):
        return False
    else:
        return True


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    matrices = np.asarray(matrices)
    vectors = np.asarray(vectors)

    ans = np.matmul(matrices, vectors).sum(axis=0)
    return ans


# tests
if notPassedTest(sum_prod(MatrixVectorBatchInput(
        matrices=[[[1, 2], [3, 4]]], vectors=[[[1], [1]]])),
        [[3], [7]]):
    print("2.1 test 1 error")
if notPassedTest(sum_prod(MatrixVectorBatchInput(
        matrices=[[[1, 0], [0, 1]], [[1, 0], [0, 1]]], vectors=[[[1], [2]], [[3], [4]]])),
        [[4], [6]]):
    print("2.1 test 2 error")
if notPassedTest(sum_prod(MatrixVectorBatchInput(
        matrices=[[[5]], [[2]], [[-1]]], vectors=[[[1]], [[2]], [[3]]])),
        [[6]]):
    print("2.1 test 3 error")
if notPassedTest(sum_prod(MatrixVectorBatchInput(
        matrices=[[[0, 0], [0, 0]], [[1, 2], [3, 4]]], vectors=[[[9], [9]], [[0], [0]]])),
        [[0], [0]]):
    print("2.1 test 4 error")


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    matrix = np.asarray(matrix)
    new_matrix = matrix.copy()

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > threshold:
                new_matrix[i, j] = 1
            else:
                new_matrix[i, j] = 0

    return new_matrix

# tests
if notPassedTest(binarize(BinarizeInput(
        matrix=[[1, 5], [3, 7]], threshold=4)),
        [[0, 1], [0, 1]]):
    print("2.2 test 1 error")
if notPassedTest(binarize(BinarizeInput(
        matrix=[[4, 4.1]], threshold=4)),
        [[0, 1]]):
    print("2.2 test 2 error")
if notPassedTest(binarize(BinarizeInput(
        matrix=[[-3, -1], [-2, 0]], threshold=-2)),
        [[0, 1], [0, 1]]):
    print("2.2 test 3 error")

test_matrix = np.array([[1, 9], [2, 8]])
binarize(BinarizeInput(matrix=test_matrix, threshold=5))
if notPassedTest(test_matrix, [[1, 9], [2, 8]]):
    print("2.2 test 4 error")

if notPassedTest(binarize(BinarizeInput(
        matrix=[[7]], threshold=7)),
        [[0]]):
    print("2.2 test 5 error")


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    matrix = np.asarray(matrix)
    ans = []

    for i in range(matrix.shape[0]):
        ans.append(np.unique(matrix[i]).tolist())

    return ans

def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    matrix = np.asarray(matrix)
    ans = []

    for j in range(matrix.shape[1]):
        ans.append(np.unique(matrix[:, j]).tolist())

    return ans

# tests
if notPassedTest(unique_rows(MatrixInput(
        matrix=[[1, 2, 2], [3, 3, 3]])),
        [[1, 2], [3]]):
    print("2.3.1 test 1 error")
if notPassedTest(unique_rows(MatrixInput(matrix=[[5]])), [[5]]):
    print("2.3.1 test 2 error")
if notPassedTest(unique_rows(MatrixInput(
        matrix=[[3, 1, 2], [1, 1, 1], [2, 1, 2]])),
        [[1, 2, 3], [1], [1, 2]]):
    print("2.3.1 test 3 error")
if notPassedTest(unique_rows(MatrixInput(
        matrix=[[-1, 0, -1, 0]])),
        [[-1, 0]]):
    print("2.3.1 test 4 error")

if notPassedTest(unique_columns(MatrixInput(
        matrix=[[1, 2], [1, 3], [1, 2]])),
        [[1], [2, 3]]):
    print("2.3.2 test 1 error")
if notPassedTest(unique_columns(MatrixInput(matrix=[[5]])), [[5]]):
    print("2.3.2 test 2 error")
if notPassedTest(unique_columns(MatrixInput(
        matrix=[[4, 4, 7]])),
        [[4], [4], [7]]):
    print("2.3.2 test 3 error")
if notPassedTest(unique_columns(MatrixInput(
        matrix=[[0, 1], [0, 1]])),
        [[0], [1]]):
    print("2.3.2 test 4 error")


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    generator = np.random.default_rng(seed)
    matrix = generator.normal(loc = mean, scale = std, size = (rows, columns))

    return MatrixStatistics(
        matrix = matrix,
        row_means = matrix.mean(axis=1),
        column_means= matrix.mean(axis=0),
        row_variances= matrix.var(axis=1),
        column_variances= matrix.var(axis=0),
    )


def histogram(stats: MatrixStatistics) -> None:
    matrix = stats.matrix
    figure, axes = plt.subplots(1, 2)

    for i in range(matrix.shape[0]):
        axes[0].hist(matrix[i], label=f"строка {i}")
    axes[0].set_title("Гистограммы по строкам")

    for j in range(matrix.shape[1]):
        axes[1].hist(matrix[:, j], label=f"столбец {j}")
    axes[1].set_title("Гистограммы по столбцам")

    plt.show()


# tests
test_stat = matrix_statistics(RandomMatrixInput(rows=3, columns=4, mean=0.0, std=1.0, seed=42))

if notPassedTest(test_stat.matrix.shape, (3, 4)):
    print("2.4 test 1 error")
if (notPassedTest(test_stat.row_means.shape, (3,))
        or notPassedTest(test_stat.column_variances.shape, (4,))):
    print("2.4 test 2 error")

test_stat_2 = matrix_statistics(RandomMatrixInput(rows=3, columns=4, mean=0.0, std=1.0, seed=42))
if notPassedTest(test_stat.matrix, test_stat_2.matrix):
    print("2.4 test 3 error")

test_stat_3 = matrix_statistics(RandomMatrixInput(rows=2, columns=3, mean=5.0, std=0.0, seed=1))
if (notPassedTest(test_stat_3.matrix, np.full((2, 3), 5.0))
        or notPassedTest(test_stat_3.row_variances, [0, 0])):
    print("2.4 test 4 error")

test_stat_4 = matrix_statistics(RandomMatrixInput(rows=1, columns=1, mean=2.0, std=3.0, seed=7))
if (notPassedTest(test_stat_4.column_variances, [0.0])
        or notPassedTest(test_stat_4.row_means, test_stat_4.matrix[:, 0])):
    print("2.4 test 5 error")

#test histigram
#histogram(test_stat)


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    i, j = np.indices((rows, columns))

    return np.where((i + j) % 2 == 0, first, second)


# tests
if notPassedTest(chess(ChessInput(
        rows=3, columns=4, first=0, second=1)),
        [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]):
    print("2.5 test 1 error")
if notPassedTest(chess(ChessInput(
        rows=1, columns=1, first=7, second=9)),
        [[7]]):
    print("2.5 test 2 error")
if notPassedTest(chess(ChessInput(
        rows=1, columns=4, first=1, second=2)),
        [[1, 2, 1, 2]]):
    print("2.5 test 3 error")
if notPassedTest(chess(ChessInput(
        rows=3, columns=1, first=1, second=2)),
        [[1], [2], [1]]):
    print("2.5 test 4 error")
if notPassedTest(chess(ChessInput(
        rows=2, columns=2, first=5, second=5)),
                 [[5, 5], [5, 5]]):
    print("2.5 test 5 error")


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color

    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    image[:, :] = background_color

    top = max((image_height - height) // 2, 0)
    left = max((image_width - width) // 2, 0)
    bottom = min(top + height, image_height)
    right = min(left + width, image_width)

    image[top:bottom, left:right] = shape_color
    return image

def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color

    image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    image[:, :] = background_color

    if semi_axis_x <= 0 or semi_axis_y <= 0:
        return image

    x0 = (image_width - 1) / 2
    y0 = (image_height - 1) / 2
    y, x = np.indices((image_height, image_width))

    inside = (x - x0) ** 2 / semi_axis_x ** 2 + (y - y0) ** 2 / semi_axis_y ** 2 <= 1
    image[inside] = shape_color
    return image

# tests
test_image = draw_rectangle(RectangleInput(width=2, height=2, image_height=4, image_width=4, shape_color=(255, 0, 0), background_color=(0, 0, 0)))
if notPassedTest(test_image.shape, (4, 4, 3)):
    print("2.6.1 test 1 error")
if notPassedTest(test_image[1:3, 1:3], np.full((2, 2, 3), [255, 0, 0])) or \
        notPassedTest(test_image[0], np.zeros((4, 3))):
    print("2.6.1 test 2 error")

test_image = draw_rectangle(RectangleInput(width=10, height=10, image_height=3, image_width=5, shape_color=(1, 2, 3), background_color=(9, 9, 9)))
if notPassedTest(test_image, np.full((3, 5, 3), [1, 2, 3])):
    print("2.6.1 test 3 error")

test_image = draw_rectangle(RectangleInput(width=0, height=0, image_height=2, image_width=2, shape_color=(1, 1, 1), background_color=(7, 7, 7)))
if notPassedTest(test_image, np.full((2, 2, 3), 7)):
    print("2.6.1 test 4 error")

test_image = draw_rectangle(RectangleInput(width=1, height=1, image_height=1, image_width=1, shape_color=(5, 6, 7), background_color=(0, 0, 0)))
if notPassedTest(test_image, [[[5, 6, 7]]]):
    print("2.6.1 test 5 error")

test_image = draw_ellipse(EllipseInput(semi_axis_x=2, semi_axis_y=2, image_height=5, image_width=5,  shape_color=(255, 255, 255), background_color=(0, 0, 0)))
if notPassedTest(test_image.shape, (5, 5, 3)):
    print("2.6.2 test 1 error")

if notPassedTest(test_image[2, 2], [255, 255, 255]) or notPassedTest(test_image[0, 0], [0, 0, 0]):
    print("2.6.2 test 2 error")

if notPassedTest(test_image[2, 0], [255, 255, 255]) or notPassedTest(test_image[0, 2], [255, 255, 255]):
    print("2.6.2 test 3 error")

test_image = draw_ellipse(EllipseInput(semi_axis_x=0, semi_axis_y=3, image_height=3, image_width=3, shape_color=(1, 1, 1), background_color=(4, 4, 4)))
if notPassedTest(test_image, np.full((3, 3, 3), 4)):
    print("2.6.2 test 4 error")

test_image = draw_ellipse(EllipseInput(semi_axis_x=100, semi_axis_y=100, image_height=2, image_width=3, shape_color=(8, 8, 8), background_color=(0, 0, 0)))
if notPassedTest(test_image, np.full((2, 3, 3), 8)):
    print("2.6.2 test 5 error")


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    values = np.asarray(values,dtype=float)
    n = len(values)

    if n == 0:
        return TimeSeriesStatistics(mean=0.0, variance=0.0, std=0.0,
            local_maxima_indices=[], local_minima_indices=[], moving_average=np.array([]))

    maxi = []
    mini = []
    for i in range(1, n - 1):
        if values[i] > values[i- 1] and values[i] > values[i + 1]:
            maxi.append(i)
        if values[i] < values[i - 1] and values[i]< values[i + 1]:
            mini.append(i)

    if window < 1 or window > n:
        moving_average = np.array([])
    else:
        moving_average = np.lib.stride_tricks.sliding_window_view(values, window).mean(axis=1)

    return TimeSeriesStatistics(
        mean=float(values.mean()),
        variance=float(values.var()),
        std=float(values.std()),
        local_maxima_indices= maxi,
        local_minima_indices=mini,
        moving_average=moving_average
    )


# tests
test_result = analyze_time_series(TimeSeriesInput(values=[1, 3, 2, 4, 1], window=2))
if (notPassedTest(test_result.local_maxima_indices, [1, 3])
        or notPassedTest(test_result.local_minima_indices, [2])):
    print("2.7 test 1 error")
if notPassedTest(test_result.moving_average, [2, 2.5, 3, 2.5]):
    print("2.7 test 2 error")
if (notPassedTest(test_result.mean, 2.2)
        or notPassedTest(test_result.std ** 2, test_result.variance)):
    print("2.7 test 3 error")

test_result = analyze_time_series(TimeSeriesInput(values=[1, 2, 2, 1], window=1))
if (notPassedTest(test_result.local_maxima_indices, []) or
        notPassedTest(test_result.local_minima_indices, [])):
    print("2.7 test 4 error")

test_result = analyze_time_series(TimeSeriesInput(values=[5], window=1))
if (notPassedTest(test_result.variance, 0.0) or
        notPassedTest(test_result.moving_average, [5])):
    print("2.7 test 5 error")

test_result = analyze_time_series(TimeSeriesInput(values=[2, 4, 6], window=3))
if notPassedTest(test_result.moving_average, [4]):
    print("2.7 test 6 error")


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    raise NotImplementedError  # TODO
