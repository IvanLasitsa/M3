'''
Як чудово, а тут вже визначені дві функції! 
Давайте скористаємося ними і напишемо програму, 
що виводить число десятків і одиниць у введеному числі!
У цій програмі не потрібно міняти визначення функцій! 
Доповніть програму так, щоб користувач міг ввести число. 
Передайте це число як параметр спочатку в функцію, 
що виводить число десятків, потім в функцію, що друкує число одиниць.
'''


def units(a):
    print("У числі " + str(a) + " " + str(a % 10) + " одиниць.")


def tens(a):
    print("У числі " + str(a) + " " + str(a % 100 // 10) + " десятків.")

number = int(input("Введіть число:"))

tens(number)
units(number)
