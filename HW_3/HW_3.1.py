"""
Задание 1.
    Реализуйте функции:
    a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
       заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
       сделайте аналитику, что заполняется быстрее и почему
       сделайте замеры времени
    b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
       получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
       сделайте аналитику, что заполняется быстрее и почему
       сделайте замеры времени
    с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
       удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
       сделайте аналитику, что заполняется быстрее и почему
       сделайте замеры времени
"""


from time import time

n = 10 ** 5


def time_decor(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer


@time_decor
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)


some_list = []
fill_list_append(some_list, n)
print('_' * 100)


@time_decor
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)


some_list = []
fill_list_insert(some_list, n)
print('_' * 100)


@time_decor
def fill_dict(dct, num):
    """Заполняет словарь"""
    for i in range(num):
        dct[i] = i


some_dict = {}
fill_dict(some_dict, n)
print('_' * 100)



@time_decor
def change_list(lst):

    for i in range(10000):
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]


change_list(some_list)
print('_' * 100)


@time_decor
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)
    for j in range(1001, 2002):
        dct[j] = 'fill'


change_dict(some_dict)
print('_' * 100)

