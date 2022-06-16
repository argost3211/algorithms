"""
задача: найти N-ое число Фибоначчи
"""


def fibonacci_recursion(n):
    if n in (1, 2):
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
