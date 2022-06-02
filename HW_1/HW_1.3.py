"""
    Задание 3.
    Для этой задачи
    1) придумайте 2-3 решения (обязательно с различной сложностью)
    2) оцените сложность каждого выражения в этих решениях в нотации О-большое
    3) оцените итоговую сложность каждого решения в нотации О-большое
    3) сделайте вывод, какое решение эффективнее и почему
    Сама задача:
    Имеется хранилище с информацией о компаниях: название и годовая прибыль.
    Для реализации хранилища можно применить любой подход,
    который вы придумаете, например, реализовать словарь.
    Реализуйте поиск трех компаний с наибольшей годовой прибылью.
    Выведите результат.
    Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


base_сompany = {
    'yandex': 5000,
    'gazprom': 5040,
    'microsoft': 2300,
    'perecrestok': 2400,
    'rosnano': 30,
    'appel': 7030,
    'samsung': 9930,
    'sochialnia_apteka': 299,
    'hiomi': 919,
    'wacom': 8901,
    'nike': 4874,
    'nokia': 6703
}


# первый вариант - O(N^2)
def sort1(base_сompany):
    list_from_dict = list(base_сompany.items())
    for i in range(len(list_from_dict)):
        lowest_value_index = i
        for j in range(i + 1, len(list_from_dict)):
            if list_from_dict[j][1] > \
                    list_from_dict[lowest_value_index][1]:
                lowest_value_index = j
        list_from_dict[i], list_from_dict[lowest_value_index] =\
            list_from_dict[lowest_value_index], list_from_dict[i]
    print(list_from_dict[0:3])


# второй вариант - O(N*logN)
def sort2(base_сompany):
    list_from_dict = list(base_сompany.items())
    list_from_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]}")


# третий вариант - O(N)
def sort3(base_сompany):
    input_max = {}
    list_d = dict(base_сompany)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    print(input_max)


sort1(base_сompany)
sort2(base_сompany)
sort3(base_сompany)


"""
Лучшим вариантом будет третий, т.к. имеет минимальную вычислительную 
сложность и решает поставленную задачу без изменение исходного словаря 
и без лишней сортировки
"""
