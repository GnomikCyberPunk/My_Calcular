print('|Сложение|\t|Вычетание|\t|Умножение|\t |Деление|\n|\t1\t |\t|\t 2\t  |\t|\t 3\t  |\t |\t 4\t |\t')
Number = int(input("Выберите цифру:\n"))
num_1 = int(input('Введите цифру: '))
num_2 = int(input('Введите цифру: '))
if Number == 1:
    print(f'{num_1} + {num_2}')
    print(num_1 + num_2)
else:
    if Number == 2:
        print(f'{num_1} - {num_2}')
        print(num_1 - num_2)
    else:
        if Number == 3:
            print(f'{num_1} * {num_2}')
            print(num_1 * num_2)
        else:
            if Number == 4:
                print(f'{num_1} / {num_2}')
                print(num_1 / num_2)
input()
