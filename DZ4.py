# Задача 22 

print('Введите разменость первого множества : ')
countN = int(input())

n = [None]*countN

print("Введите первый набор чисел")
for i in range(countN):
    n[i] = int(input())

print('Введите разменость второго множества : ')
countM = int(input())

m = [None]*countM

print("Введите второй набор чисел ")
for i in range(countM):
    m[i] = int(input())

m = list(set(m))
m = set(m)

n = list(set(n))
n = set(n)

result = list(m.intersection(n))

print(sorted(result))

# задача 24

print("Введите количество кустов : ")
n = int(input())

list = list(range(1, n+1))

print("Количество ягод на каждом кусте")
print(list)

max = 0

for i in range(1, 4):
    max += list[-i]

print(f'Маусимальное число ягод за один заход {max}')

