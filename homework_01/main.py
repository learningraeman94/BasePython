"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    """
    Просто́е число́ — натуральное (целое положительное) число, 
    имеющее ровно два различных натуральных делителя — единицу и самого себя.
    Другими словами, число x является простым, если оно больше 1 
    и при этом делится без остатка только на 1 и на x.
    """
    k = 0
    for i in range(2, n // 2+1):
        if (n % i == 0):
            k = k+1
    return True if n > 1 and k <= 0 else False

def filter_numbers(numlist,type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type == ODD:
        return [i for i in numlist if i % 2 == 1]
    elif type == EVEN:
        return [i for i in numlist if i % 2 != 1]
    elif type == PRIME:
        return list(filter(is_prime,numlist))
        # return [i for i in numlist if is_prime(i)]


# print(power_numbers(1, 2, 5, 7))
# print(filter_numbers([1, 2, 5, 7],ODD))
# print(filter_numbers([1, 2, 5, 8],EVEN))
# # 2, 3, 5, 7, 11, 13
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(filter_numbers(my_list,PRIME))
