'''
Збережіть програму як модуль з ім'ям birthday.
Настав час створити свій перший модуль! 
Перед Вами програма, яка допомагає визначити, 
в яку пору року і в який день тижня народилася людина.
Збережіть її як модуль з ім'ям birthday і переходьте
до наступного завдання !
'''

# Функція повертає рядок з назвою пори року, коли народилася людина



import birthday

m = int(input("Введіть номер місяця народження: "))
d = int(input("Введіть номер дня тижня народження: "))

season_result = birthday.season(m)
day_result = birthday.day(d)

print(f"Ви народились в {season_result}, в {day_result}.")
