"""
Задача: найти максимально число в массиве
"""

myList = [1, 2, 3, 4, 6]
myList.sort()


def find_max(numbers: list) -> int:
    max_number = float("-inf")
    for number in numbers:
        max_number = number if number > max_number else max_number
    return max_number


if __name__ == '__main__':
    print(find_max(myList))
