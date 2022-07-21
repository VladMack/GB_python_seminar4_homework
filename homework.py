# Вычислить число c заданной точностью d

from random import randint
d = int(input('Введи количество чисел после запятой: '))
g = 0
for i in range(1, 10**d):
    g += 1 / (i**2)
pi = (g * 6)**0.5
print(round(pi, d))

# 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых делителей числа N. (1 - составное число)


def prime_check(number):
    for i in range(int(number ** 0.5), 1, -1):
        if number % i == 0:
            return False
    return True


def find_divs(number):
    divs = []
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:
            if prime_check(i):
                divs.append(i)
    return divs


num = int(input('Введи число: '))
print(find_divs(num))

# 2. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.


def uniq_values(arr1):
    l_uniq_values = []
    for i in range(0, len(arr1)):
        flag = 0
        for j in range(0, len(arr1)):
            if arr1[j] == arr1[i] and i != j:
                flag = 1
                break
        if flag == 0:
            l_uniq_values.append(arr1[i])
    return l_uniq_values


list1 = ['1', 1, 1.0, '1', 11, '1', 2, 3]
print(list1)
print('Неповторяющиеся члены последовательности:')
print(uniq_values(list1))


# 3. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.

k = int(input())

mnogochlen = ''
for i in range(k, 1, -1):
    mnogochlen += f'{randint(0, 101)}x^{i} + '
mnogochlen += f'{randint(0, 101)}'
print(mnogochlen)
