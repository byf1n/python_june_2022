# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# print(','.join(el for el in st if el.isdigit() == True))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st1 = 'as21 2121 23 1212fdf212dg544'
# print(','.join(''.join(ch if ch.isdigit() else ' ' for ch in st1).split()))

# #################################################################################
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#

# greeting = 'Hello, world'
# print([ch.upper() for ch in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([num**2 for num in range(50)])

# function
#
# - створити функцію яка виводить ліст

# def show (ls):
#     print(ls)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def maxNum (a,b,c):
#     max1 = max(a,b,c)
#     print(max1)
#     return max1

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def maxMin (*args):
#     print(max(args))
#     return min(args)


# - створити функцію яка повертає найбільше число з ліста

# def maxList (ls):
#     print(max(ls))

# - створити функцію яка повертає найменьше число з ліста

# def minList (ls):
#     print(min(ls))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sumlist (ls):
#     print(sum(ls))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#

# def avgList (ls):
#     return sum(ls) / len(ls)


# ################################################################################################
# 1)Дан list:
# list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'

def minNum():
    ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(f'min num: {min(ls)}')


def delDublicate():
    ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(list(set(ls)))


def change():
    ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(['X' if (i + 1) % 4 == 0 else v for i, v in enumerate(ls)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(num):
    print('*' * num)
    for i in range(num - 2):
        print('*' + ' ' * (num - 2) + '*')
    print('*' * num)


# 3) вывести табличку множення за допомогою цикла while

def table():
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            res = i * j
            print(f'{res:4}', end='')
            j+=1
        i+=1
        print(' ')

# 4) переробити це завдання під меню
while True:
    num = int(input('num from 1 to 5, exit - 0: '))
    if num == 1:
        minNum()
    elif num == 2:
        delDublicate()
    elif num == 3:
        change()
    elif num == 4:
        lenght = int(input('lenght: '))
        square(int(lenght))
    elif num == 5:
        table()
    elif num == 0:
        break
    else:
        print('not expected num')
        num = int(input('num from 1 to 5, exit - 0: '))