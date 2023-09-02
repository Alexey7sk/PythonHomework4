# Задача 22: Даны два неупорядоченных набора целых 
# чисел (может быть, с повторениями). Выдать без 
# повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов 
# первого множества. m — кол-во элементов второго 
# множества. Затем пользователь вводит сами 
# элементы множеств.

n = (int(input('Введите количество элементов N: ')))
num_list_1 = []
for i in range(n):
    num = int(input('Введите числа поочереди '))
    num_list_1.append(num)
print(num_list_1)

m = (int(input('Введите число M элементов: ')))
num_list_2 = []
for i in range(m):
    num = int(input('Введите числа поочереди '))
    num_list_2.append(num)
print(num_list_2)
print()

num_list_3 = num_list_1 + num_list_2
check_list = []
for i in num_list_3:
    if num_list_3.count(i) > 1 and i not in check_list:
        check_list.append(i)
        print(i)
