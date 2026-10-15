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
histogram(test_stat)


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    raise NotImplementedError  # TODO


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    raise NotImplementedError  # TODO


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    raise NotImplementedError  # TODO


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    raise NotImplementedError  # TODO


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    raise NotImplementedError  # TODO
