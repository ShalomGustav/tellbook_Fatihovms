with open('tell_book.txt', 'r') as file:
    print('Введите номер телефона для замены данных')
    n = input(': ')
    for line in file:

        if n in line:
            print('Замените номер телефона', n, 'на новый')
            new_n = input(': ')
            line.replace(n, new_n)