# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


my_list = []
a1 = (int(input('Введите первый элемент арифметической прогрессии: ')))
d = (int(input('Введите разность арифметической прогрессии: ')))
n = (int(input('Введите количество элементов арифметической прогрессии: ')))
for i in range(n):
    my_list.append(a1 + (i) * d)
    
print(my_list)