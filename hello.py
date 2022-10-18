from cgitb import text
from fileinput import close
from turtle import clear
from unittest.mock import patch


# print ( "hello world" )


# Переменные
# Типы данных справедливы
# from email.quoprimime import body_length
# from xmlrpc.client import Boolean


# int, float, Boolean, str,
# list и др

# Python-язык с динамической типизацией




# Value = 2809
# name = "Sergey"
# Value = None

# print (type (Value))
# print (type (a))
# print (type (b))
# Value = 12334
# print (type (Value))
# s = 'hello world'

# a = 123
# b = 1.23

# print (s) # вывод строки 
# print (a, '-', b, '-', s,)
# print ('{1} - {2} - {0} '.format (a, b, s))
# print (f'{a} - {b} - {s}')

# f = False
# print(f)


# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print (list)
# print (col)


# Ввод и вывод данных
# print-отвечает за вывод данных
# input- отвечает за ввод данных


# print ('Введите а')
# a = float (input ())
# print ('Введите b')
# b = float (input ())
# print (a, '+' , b, '=' , a + b)
# print ( '{} {}'.format (a, b))
# print (f'{a} {b}')



# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной программы 
# Если помните математику-проблем не будет
# +, -, *, /, %, //, **
# Приоритет операций
# **, ㊉, ㊀, *, /, //, %, +, -
# Скобки меняют приоритет

# a = 1.3123123
# b = 3
# c = round (a*b, 7)
# print (c)


# a = 2
# b =  8
# c = a + b
# print (c)


# a = int (input( 'a = '))
# b = int (input( 'b = '))
# if a > b:
#     print (a)
# else:
#     print (b)


# username = input ('Введите имя')
# if username == 'Маша':
#     print ('Ура, это же Маша!') 
# elif username == 'Марина':
#     print ('Я так ждал Вас, Марина!') 
# elif username == 'Мурат':
#     print ('Мурат - топ')
# else:
#     print ('Привет, ' , username)

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else: 
#     print (' Пожалуй')
#     print ('[dfnbn')
# print (inverted)



# for i in 1,2,3,4,5:
#     print(i**2)


# r = range(10)
# for i in r:
#     print (i)
    

    # или 


# for i in range (10):
#     print (i)


# for i in range (1,  10,  2 ):
#     print (i)




# print (len (text))                      #39
# print ( 'еще' in text)                  #True
# print ( text.isdigit ())                #Fasle
# print ( text.islower ())                #True
# print (text.replase ('еще' 'ЕЩЕ'))      #



# def f(x):
#     if x ==1:
#         return 'Целое'
#     elif x ==2.3:
#         return 23
#     else:
#         return

# arg = 2
# print (f (arg))
# print (type(f(arg)))




# colors = ['red', 'green', 'biue' ]
# data = open ('file.txt', 'w')
# data.writelines (colors)     #разделителей не будет
# data.close()

# exit()
# patch = 'file.txt'
# data = open(patch, 'r')
# for line in data:
#     print (line)
# data.close ()



# colors = ['red', 'green', 'biue' ]
# data = open ('file.txt', 'w')
# data.write ('LINE 2\n')  
# data.write ('LINE 3\n')    
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print (line)
# data.close ()

# exit()



# def f(x):
#     if x ==1:
#         return 'Целое'
#     elif x ==2.3:
#         return 23
#     else:
#         return

# arg = 2
# print (f (arg))
# print (type(f(arg)))


# import hello 

# print (hello.f(1))


# a = 3, 4
# print (a)








# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# x = [2, 3, 6, 10, 12, 16, 5]
# #print(x)
# summ = 0
# for i in range(1, len(x), 2):
#     #if i % 2 == 1:
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")





# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)




#  Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print(max-min)



#  Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)




# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")




# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")




# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# import random


# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))




# Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# x, y = 4, 6
# if x > y: big_num = x
# else: big_num = y
# while(True):
#     if (big_num % x == 0) and (big_num % y == 0):
#         result = big_num
#         break
#     big_num += 1
# print(result)







# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# вариант человек против человека:
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

# with open('file_encode.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')




# Напишите программу, удаляющую из текста все слова содержащие "абв".

# def Del_Word(s):
#     return False if 'абв' in s else True
#     #for i in range(len(s)-2):
#     #    if (s[i]+s[i+1]+s[i+2]) == 'абв':
#     #        f =  False
#     #return f


# print('Введите текст ')
# a = input()

# a = a.split()
# print(a)
# a = list(filter(Del_Word,a))
# print(a)




# Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# *Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.*
# ***Порядок элементов менять нельзя***

# nums = [3, 1, 2, 3, 4, 6, 1, 7]

# # Первый вариант

# def get_up2(nums):
#     ups = [nums[0]]
#     for i in nums:
#         if i > max(ups):
#             ups.append(i)
#     return ups
    
# print(get_up2(nums))

# # Второй вариант

# def get_up(nums):
#     ups = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
#             ups.append(nums[i])
#     return ups

# print(get_up(nums))










