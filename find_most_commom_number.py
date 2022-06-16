"""
Задача: в последовательности есть число, которое втречается БОЛЬШЕ ПОЛОВИНЫ РАЗ, найти это число
"""

l = [1, 2, 100, 100, 100, 100, 1, 2, ]  # 100
l1 = [100, 1, 1, 1, 100, 100, 100, 100, 1]  # 100


def find_frequent_element(numbers: list):
    element = None
    count = 0
    for i in range(len(numbers)):
        if count == 0:
            element = numbers[i]
            count += 1
        elif element == numbers[i]:
            count += 1
        else:
            count -= 1
    return element


if __name__ == '__main__':
    print(find_frequent_element(l1))

