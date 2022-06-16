"""
Задача: в массиве записаны целые числа, всех по 2 кроме числа, что записано 1 раз, найти это число
"""

myList = [1, 1, 2, 2, 5, 3, 4, 4, 3]


def find_number(numbers: list) -> int:
    number = 0
    for index in range(len(numbers)):
        number ^= numbers[index]
        print(number)
    return number


if __name__ == '__main__':
    print(find_number(myList))