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
























