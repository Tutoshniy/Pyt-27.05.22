#1 Найти сумму чисел списка стоящих на нечетной позиции
#list = []
# sum = 0
def vvod(): #функция заполнения массива
    n = int(input("Введите количество чисел: "))
    print("Вводите числа")
    for i in range(n):
        list.append(int(input()))
# vvod()
# print(list)
# for i in range(len(list)):
#     if i%2 == 0:                  решение первого номера
#         sum+=list[i]              функция я использовал в следующих номерах
# print(sum)

#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
#второй и предпоследний
# list = []                         Решение второго номера
# result = []
# vvod()
# for i in range(len(list)//2+len(list)%2):
#     result.append(list[i] * list[len(list)-i-1])
# print(result)

#3 В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной

# list = []
# veshnums = []
# max = 0.0000000001
# min = 1
# n = int(input("Введите количество чисел: "))
# for i in range(n):                  #здесь наша функция не сработает,
#     list.append(float(input()))     #поэтому я написал новое
#     if (list[i]-int(list[i])) != 0:
#         veshnums.append(round(list[i]-int(list[i]), 3))
# for i in range(len(veshnums)):
#     if veshnums[i] < min: min = veshnums[i]
#     if veshnums[i] > max: max = veshnums[i]
# print(round(max - min, 3))

#4 Написать программу преобразования десятичного числа в двоичное
# N = int(input("Введите число: "))
# dvoich = []
# while N != 0:
#     dvoich.append(N%2)
#     N//=2
# for i in range(len(dvoich)):
#     print(dvoich[len(dvoich)-i-1], end='')

#Экстра 1 Написать программу преобразования двоичного числа в десятичное.
N = input("Введите число: ")
fin = 0
for i in range(len(N)):
    fin = fin + (2**(len(N)-i-1))*int(N[i])
print(fin)
