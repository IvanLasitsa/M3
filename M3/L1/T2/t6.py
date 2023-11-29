'''
Користувач вводить чотиризначне число. 
Виведіть число, складене з тих самих цифр, 
записаних в зворотному порядку.
Рішення оформи у вигляді функції reverse (n), 
яка отримує на вхід введене користувачем число 
і повертає його перевертень.
'''

def reverse(n):
    str_n = str(n)

    reversed_str = str_n[::-1]

    reversed_num = int(reversed_str)

    return reversed_num

user_number = int(input("Введіть чотиризначне число: "))

result = reverse(user_number)
print("Результат:", result)
