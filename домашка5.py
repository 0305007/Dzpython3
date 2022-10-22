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


