#Задача 22: Даны два неупорядоченных набора целых чисел (может
#быть, с повторениями). Выдать без повторений в порядке возрастания
#все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого
#множества. m — кол-во элементов второго множества.
#Затем пользователь вводит сами элементы множеств.

print("Введите количество элементов первого множества n: ")
n = int(input())
print("Введите количество элементов второго множества m: ")
m = int(input())

set1 = set()
set2 = set()

print("Введите элементы первого множества n: ")
for i in range(n):
    number = int(input())
    set1.add(number)
print("Введите элементы второго множества m: ")
for i in range(m):
    number = int(input())
    set2.add(number)

common_elem = []
for number in set1:
    if number in set2:
        common_elem.append(number)

def quick_sort (arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
sorted_com_el = quick_sort(common_elem)
print(sorted_com_el)