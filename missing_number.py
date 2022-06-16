"""
Задача: в строке числа от 1 до N, нужно найти пропущенное число
"""


myList = [8, 2, 3, 4, 6, 7, 1]

N = 8


def missing_number_v1(numbers: list, n: int) -> int:
    for number in list(range(1, n + 1)):
        if number not in numbers:
            return number


def missing_number_v2(numbers: list, n: int) -> int:
    return sum(range(1, n + 1)) - sum(numbers)


if __name__ == '__main__':
    missing_number_v1(myList, N)
    missing_number_v2(myList, N)

