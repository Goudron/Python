from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавлены в {var} файл')



def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))

def del_data():
    num = int(input('Введите # элемента для удаления: ')) - 1
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
    with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
        for i in range(num * 5):
            file.write(data[i])
        for i in range((num + 1) * 5, len(data)):
            file.write(data[i])

def mod_data():
    num = int(input('Введите # элемента для изменения: ')) - 1
    name, surname, phone, adress = input_user_data()
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
    with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
        for i in range(num * 5):
            file.write(data[i])
        file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
        for i in range((num + 1) * 5, len(data)):
            file.write(data[i])
