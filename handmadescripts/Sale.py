
#          Магазин SALE% SALE% SALE% 

# переменные №1,№2 скидки в процентах
choise1 = 10
choise2 = 50
# тип данных   ввод пользователя
guess = int(input('Введите вашу сумму '))
# логический оператор "если"
if guess >= 5000:  # деление /
    totalprice = guess / choise2 - guess
    print(f'Итого: {totalprice}')
# логический оператор "а если"
elif guess >= 1000: # деление /
    totalprice = guess / choise1 - guess
    print(f'Итого: {totalprice}')
# логический оператор "иначе" мусорное ведро куда попадает прочее
else:
    print(f'Итого: {guess}')
# print вывод
print('Завершено ')

# %%



