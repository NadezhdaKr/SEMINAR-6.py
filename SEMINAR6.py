# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.

user_input = input("Введите число: ")
result = int(user_input) + int(user_input * 2) + int(user_input * 3)
print(result)



# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

numbers = [random.randint(0, 9) for i in range(15)]
numbers_str = ''.join(map(str, numbers))
print(numbers)
number_str = input('Введитете натуральное число: ')

if number_str in numbers_str:
     print('да')
else:
     print('нет')


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def farey(n, asc=True):
     if asc:
         a, b, c, d = 0, 1, 1, n
     else:
         a, b, c, d = 1, 1, n - 1, n
     print(f"{a}/{b}", end=", ")
     while (asc and c <= n) or (not asc and a > 0):
         k = int((n + b) / d)
         a, b, c, d = c, d, k * c - a, k * d - b
         print(f"{a}/{b}", end=", ")


user_number = int(input("Введите знаменатель: "))
farey(user_number)
