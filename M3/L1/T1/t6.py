'''
Ми створювали чат-бота для допомоги нам в математиці. 
Давайте напишемо йому нову команду, яка буде порівнювати два числа!
У програмі вже є запит введення двох чисел і передача їх в функцію як параметри. 
Ваше завдання - визначити функцію more_less. 
Якщо a > b, функція повинна друкувати рядок "a більше b". 
Якщо a < b, функція повинна друкувати рядок "a менше b". 
Якщо a == b, функція повинна друкувати рядок "a дорівнює b".
'''

def more_less(a, b):
    if a > b:
        print(f"{a} більше {b} ")
    elif a < b:
        print(f"{a} менше {b} ")
    else:
        print(f"{a} дорівнює {b} ")

a = int(input("Введіть число 1: "))
b = int(input("Введіть число 2: "))
more_less(a, b)
