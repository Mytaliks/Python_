"""
    Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
    натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
    где n - любое натуральное число.
"""

def recur_method(numb):
    if numb == 1:
        return numb
    else:
        return recur_method(numb - 1) + numb


try:
    NUMB = int(input("Введите число: "))
    if recur_method(NUMB) == NUMB * (NUMB + 1) / 2:
        print('Равенство верно!!!')
except ValueError:
    print("Вы вместо числа ввели строку(. Исправьтесь!")


