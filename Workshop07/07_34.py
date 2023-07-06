# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

#Формирование множества гласных
vowel = 'аяуюоеёэиы'
vowel_set = set()
for i in range(len(vowel)):
    vowel_set.add(vowel[i])

#Ввод строки
poem = str(input('Введите стихотворение: '))

#Разбиение стихотворения на фразы
phrases = poem.split(' ')

#Функция определения количества гласных в фразе
def vowel_phrase(string):
    count = 0
    for i in range(len(string)):
        if string[i] in vowel_set:
            count += 1
    return count

#Определение ритмичности стихотворения
vowel_0 = vowel_phrase(phrases[0])
res_list = list(filter(lambda x: vowel_phrase(x) != vowel_0, phrases))

#Вывод результата
if len(res_list) == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')