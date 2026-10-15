"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput

def notPassedTest(functionOutput, expectedOutput) -> bool:
    if(functionOutput == expectedOutput):
        return False
    else:
        return True

def count_vowels(data: TextInput) -> int:
    if data.value is None:
        return 0
    text = data.value.lower()
    counter = 0

    for i in range(len(text)):
        if text[i] in 'aeiou':
            counter+=1
        else:
            continue
    return counter

#tests
if notPassedTest(count_vowels(TextInput('')),0):
    print("1.1 test 1 error")
if notPassedTest(count_vowels(TextInput('AAAaaa')), 6):
    print("1.1 test 2 error")
if notPassedTest(count_vowels(TextInput('one phrase')), 4):
    print("1.1 test 2 error")


def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    unique = []

    for i in range(len(text)):
        if text[i] in unique:
            return False
        else:
            unique.append(text[i])

    return True

#tests
if notPassedTest(has_unique_characters(TextInput('')), True):
    print("1.2 test 1 error")
if notPassedTest(has_unique_characters(TextInput('abcdefg')), True):
    print("1.2 test 2 error")
if notPassedTest(has_unique_characters(TextInput('abcda')), False):
    print("1.2 test 3 error")
if notPassedTest(has_unique_characters(TextInput('Aa')), True):
    print("1.2 test 4 error")
if notPassedTest(has_unique_characters(TextInput('a b c ')), False):
    print("1.2 test 5 error")

def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    bits = []
    while (number > 0):
        bits.append(number % 2)
        number = number // 2
    return bits.count(1)

#tests
if notPassedTest(count_one_bits(PositiveIntegerInput(0)), 0):
    print("1.3 test 1 error")
if notPassedTest(count_one_bits(PositiveIntegerInput(1)), 1):
    print("1.3 test 2 error")
if notPassedTest(count_one_bits(PositiveIntegerInput(16)), 1):
    print("1.3 test 3 error")
if notPassedTest(count_one_bits(PositiveIntegerInput(15)), 4):
    print("1.3 test 4 error")
if notPassedTest(count_one_bits(PositiveIntegerInput(42)), 3):
    print("1.3 test 5 error")

def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    steps = 0

    while number >= 10:
        product = 1
        current = number
        while current > 0:
            product *= current % 10
            current //= 10

        number = product
        steps += 1

    return steps


# tests
if notPassedTest(multiplicative_persistence(PositiveIntegerInput(4)), 0):
    print("1.4 test 1 error")
if notPassedTest(multiplicative_persistence(PositiveIntegerInput(39)), 3):
    print("1.4 test 2 error")
if notPassedTest(multiplicative_persistence(PositiveIntegerInput(999)), 4):
    print("1.4 test 3 error")
if notPassedTest(multiplicative_persistence(PositiveIntegerInput(25)), 2):
    print("1.4 test 4 error")


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    n = len(predicted)
    if n == 0:
        return 0.0

    sum = 0
    for i in range(n):
        sum += (predicted[i] - expected[i]) ** 2

    return sum / n


# tests
if notPassedTest(mse(VectorPairInput(predicted=[1, 2, 3], expected=[1, 2, 3])), 0.0):
    print("1.5 test 1 error")
if notPassedTest(mse(VectorPairInput(predicted=[2, 3, 4], expected=[1, 2, 3])), 1.0):
    print("1.5 test 2 error")
if notPassedTest(mse(VectorPairInput(predicted=[0, 2], expected=[3, 0])), 6.5):
    print("1.5 test 3 error")
if notPassedTest(mse(VectorPairInput(predicted=[-1, -2], expected=[1, 2])), 10.0):
    print("1.5 test 4 error")


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    if number == 1:
        return "(1)"

    result = ""
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            degree = 0
            while number % divisor == 0:
                degree += 1
                number //= divisor

            if degree == 1:
                result += f"({divisor})"
            else:
                result += f"({divisor}**{degree})"

        divisor += 1

        if divisor * divisor > number and number > 1:
            result += f"({number})"
            break

    return result


# tests
if notPassedTest(prime_factorization(PositiveIntegerInput(86240)), "(2**5)(5)(7**2)(11)"):
    print("1.6 test 1 error")
if notPassedTest(prime_factorization(PositiveIntegerInput(13)), "(13)"):
    print("1.6 test 2 error")
if notPassedTest(prime_factorization(PositiveIntegerInput(9)), "(3**2)"):
    print("1.6 test 3 error")
if notPassedTest(prime_factorization(PositiveIntegerInput(1)), "(1)"):
    print("1.6 test 4 error")


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    sum = 0
    k = 1

    while sum < cube_count:
        sum += k ** 2
        if sum == cube_count:
            return k
        k += 1

    return "It is impossible"


# tests
if notPassedTest(pyramid(PositiveIntegerInput(1)), 1):
    print("1.7 test 1 error")
if notPassedTest(pyramid(PositiveIntegerInput(5)), 2):
    print("1.7 test 2 error")
if notPassedTest(pyramid(PositiveIntegerInput(14)), 3):
    print("1.7 test 3 error")
if notPassedTest(pyramid(PositiveIntegerInput(4)), "It is impossible"):
    print("1.7 test 4 error")
if notPassedTest(pyramid(PositiveIntegerInput(100)), "It is impossible"):
    print("1.7 test 5 error")


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    s = str(data.value)
    mid = len(s) // 2

    if len(s) % 2 == 1:
        left = s[:mid]
        right = s[mid + 1:]
    else:
        left = s[:mid - 1]
        right = s[mid + 1:]

    return sum(map(int, left)) == sum(map(int, right))

# tests
if notPassedTest(is_balanced_number(PositiveIntegerInput(1234006)), True):
    print("1.8 test 1 error")
if notPassedTest(is_balanced_number(PositiveIntegerInput(123456)), False):
    print("1.8 test 2 error")
if notPassedTest(is_balanced_number(PositiveIntegerInput(1)), True):
    print("1.8 test 3 error")
if notPassedTest(is_balanced_number(PositiveIntegerInput(11)), True):
    print("1.8 test 4 error")
if notPassedTest(is_balanced_number(PositiveIntegerInput(50905)), True):
    print("1.8 test 5 error")
