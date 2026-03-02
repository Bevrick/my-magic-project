# calculzen
# Калькулятор сбережений

money = int(input('Сколько денег ты готов откладывать каждый день? '))
print(f"{money} zeny")
# ввод записанный в метод input записывается в перемнную

days = int(input('Сколько дней необходимо? '))
print(f"{days} days")

totalprice = days * money
# производение можно записывать в отдельную переменную

print(f"Your money {totalprice}")
# f строки можно переносить в начало и в конец блока
