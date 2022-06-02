"""
    Задание 2.
    Реализуйте два алгоритма.
    Оба должны обеспечивать поиск минимального значения для списка.
    Сложность первого алгоритма должна быть O(n^2) - квадратичная.
    Сложность второго алгоритма должна быть O(n) - линейная.
"""

from random import randint

def list_min_f(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i


def list_min_s(lst_t):
    min_value = lst_t[0]
    for i in lst_t:
        if i < min_value:
            min_value = i
        return min_value


lst1 = [randint(0, 40) for i in range(20)]
lst2 = [randint(0, 50) for i in range(20)]
print(lst1)
print(lst2)