

from random import randint
from timeit import timeit



def reverse_sort(lst_obj):
    ordered_list = sorted(lst_obj)
    return ordered_list


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))
