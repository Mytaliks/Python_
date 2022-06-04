"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
"""

def revers_number(numb):
    rest_numb, numeral = divmod(numb, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(revers_number(rest_numb))



number = int(input(" Введите число, которое требуется перевернуть: "))
print(f'Перевернутое число: {revers_number(number)}')
