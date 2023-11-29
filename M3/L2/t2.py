'''
Напишіть функцію
Програма просить ввести число n і друкує всі числа від n до 1 включно
'''

def print_numbers_reverse(n):
    for i in range(n, 0, -1):
        print(i)

user_input = int(input("Введіть число n: "))

print_numbers_reverse(user_input)
