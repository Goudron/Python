# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во элементов первого набора: '))
m = int(input('Введите кол-во элементов второго набора: '))
set_n = set()
set_m = set()

for i in range (n):
    set_n.add(int(input('Введите элемент первого набора: ')))
for i in range (m):
    set_m.add(int(input('Введите элемент второго набора: ')))

set_intersec = set_n.intersection(set_m)

list_intersec = list(set_intersec)
list_intersec.sort()

for i in range(len(list_intersec)):
    print(list_intersec[i], end = ' ')
