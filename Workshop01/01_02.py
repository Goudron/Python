# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите число: '))
first = n // 100
n = n - 100 * first
second = n // 10
third = n - 10 * second
print (first + second + third)
