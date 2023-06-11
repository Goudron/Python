# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

num = int(input('Введите номер билета: '))

t1 = num // 1000
first = t1 // 100
second = t1 // 10 % 10
third = t1 % 10

t2 = num % 1000
fourth = t2 // 100
fifth = t2 // 10 % 10
sixth = t2 % 10

if first + second + third == fourth + fifth + sixth:
    print ('y')
else:
    print ('n')
