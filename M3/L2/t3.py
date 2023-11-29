'''
Потрібно порахувати добуток чисел від a до b. 
Програма запитує числа і виводить результат.
Програма запитує у людини спочатку перше число, потім друге. 
Після цього програма повинна перемножити всі числа від a до b 
(припускаючи, що a < b) і надрукувати результат. 
Приклад: Введено числа 5 і 7. 
Програма надрукує "210" (5 * 6 * 7 = 210).
'''

def calculate_product(a, b):
    product = 1
    for num in range(a, b + 1):
        product *= num
    return product

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

if a < b:
    result = calculate_product(a, b)
    print(f"Добуток чисел від {a} до {b} включно: {result}")
else:
    print("Перевірте введені числа. a повинно бути менше за b.")