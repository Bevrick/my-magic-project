number = 23
# цикл while проверяет логическое условие boolean
while True:
    # инструмент try... except игнорирует ошибку
    try:
        guess = int(input('Введите число: '))
    except ValueError:
        print('Возникла ошибка! ')
        # continue продолжает цикл       
        continue
    # проверяет условие boolean
    if guess == number:
        print('Шалость удалась! ')
        print('Программа завершена ')
        break
    # эта строка лишняя, но она работает
    if guess < number:
        print('Не верно!' )
    else:
        print('Не верно! ')
    
