from logger import input_data, print_data, del_data, mod_data

def interface():
    print('Добрый день! Это бот-помощник.\n'
          'Что Вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные\n'
          '3 - Удалить данные\n'
          '4 - Изменить данные\n')
    
    command = int(input('Ваш выбор: '))

    while 1 > command > 5:
        command = int(input('Ошибка! Попробуйте ещё раз! Ваш выбор: '))

    match command:
        case 1:
            input_data()
        case 2:
            print_data()
        case 3:
            del_data()
        case 4:
            mod_data()
