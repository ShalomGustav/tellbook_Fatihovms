def new_write_file_name():# Функция записи в файл новых пользователей
    names = list()
    numbers = list()
    names_numbers = list()
    count = int(input('Введите количество пользователей которых нужно добавить:'))

    for name in range(count):
        print('Добавьте ФИО:')
        names.append(input(': '))
        print('Добавьте номер:')
        numbers.append(input(': '))
    for name_number in range(count):
        names_numbers += ['ФИО: ' + names[name_number] + ' Номер: ' + numbers[name_number]]

    with open('tell_book.txt','a', encoding='utf-8') as file:#открытие файла на дозапись
        for name_num in names_numbers:
            file.write(name_num + '\n')
    return print('Данные успешно добавлены!')

def delete_with_file():#удаление данных из файла
    with open('tell_book.txt', 'w', encoding='utf-8') as file:
        file.truncate()
        file.close()

def search_in_file():#поиск данных в файле
    with open('tell_book.txt', encoding='utf-8') as file:
        print('Введите номер телефона для поиска')
        n = input(': ')
        for line in file:
            if n in line:
                print(line)

def replace_in_file_data():#замена данных в файле(номер телефона)
    with open('tell_book.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print('----------------------------------')
        print('--------ТЕЛЕФОННАЯ КНИГА----------')
        print( *lines)
        print('----------------------------------')
        n = input('Введите номер телефона для замены: ')

        new_n = input('Введите новый номер: ')

        for line in range(len(lines)):
            if n in lines[line]:
                lines[line] = lines[line].replace(n,new_n)
            

    with open('tell_book.txt', 'w', encoding='utf-8'), open('tell_book.txt', 'a', encoding='utf-8') as file:  # открытие файла на дозапись
        for name_num in lines:
            file.write(name_num)
    return print('Данные успешно изменены!')



def print_my_tell_book():#вывод данных в файле
    with open('tell_book.txt', 'r', encoding='utf-8') as file:
        print('Вашa телефоная книга: ')
        count = 0
        for line in file:
            count+=1
            print(count, line)

def main():
    print('Выберите действие:')
    print('Добавить данные в телефонную книгу - 1')
    print('Очистить все данные из телефонной книги - 2')
    print('Поиск данных по номеру телефона - 3')
    print('Показать телефонную книгу - 4')
    print('Изменение данных по номеру телефона - 5')
    n = int(input('Выберите действие: '))
    if n == 1:
        new_write_file_name()
    if n == 2:
        delete_with_file()
    if n == 3:
        search_in_file()
    if n == 4:
        print_my_tell_book()
    if n == 5:
        replace_in_file_data()

if __name__ == '__main__':
    main()







