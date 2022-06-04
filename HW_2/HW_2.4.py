"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f"Количество элементов - {n_count}, сумма - {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum+numb)


try:
    N_COUNT = int(input("Введите количество элементов: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")
