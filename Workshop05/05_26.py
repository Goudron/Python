# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def power(n, m):
    if m == 1:
        return n
    return n * power(n, m - 1)

A = int(input('Введите основание степени: '))
B = int(input('Введите показатель степени: '))

print(power(A, B))
