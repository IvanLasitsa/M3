'''
Програма повинна вивести площу прямокутного трикутника з заданими катетами. 
Чому вона повертає неправильне число? 
Знайдіть і виправте всі помилки.
'''


def area_tr(a, b):
    ans = (a * b) / 2
    return ans

result = area_tr(4, 5)
print(result)

