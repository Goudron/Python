# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

N = int(input('Введите количество кустов: '))
a = list()
for i in range(N):
    a.append(int(input('Введите количество ягод на кусте: ')))
max = 0

for i in range(1, N + 1):
    if a[(i - 1) % N] + a[i % N] + a[(i + 1) % N] > max:
        max = a[(i - 1) % N] + a[i % N] + a[(i + 1) % N]

print(max)
