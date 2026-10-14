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
    raise NotImplementedError  # TODO


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    raise NotImplementedError  # TODO


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    raise NotImplementedError  # TODO


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    raise NotImplementedError  # TODO
