#Задание 16

print("Введите размерность массива : ")
n = int(input())

a = [None] * n

print("Заполнение массива : ")
for i in range(len(a)):
    print(f"A[{i}]")
    a[i] = int(input())

print("Введите число для поиска : ")
x = int(input())

count = 0

for i in range(len(a)):
    if(a[i] == x):
        count += 1

print(f"Число {x} встречается {count} раз")

# Задание 18

print("Введите размерность массива : ")
n1 = int(input())

a1 = [None] * n1

print("Заполнение массива : ")
for i in range(len(a1)):
    print(f"A[{i}]")
    a1[i] = int(input())

print("Введите число для поиска : ")
x1 = int(input())

a1.sort()
print(a1)

findmin = 0
findmax = 0

for i in range(len(a1)):
    if(a1[i] < x1):
        findmin = a1[i]
    else:
        findmax = a1[i]
        continue

if(x1-findmin > findmax-x1):
    print(findmax)
else:
    print(findmin)
        
# Задание 20

d_en = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
     2: ['D', 'G'],
     3: ['B', 'C', 'M', 'P'],
     4: ['Й', 'Ы'],
     5: ['K'],
     8: ['J', 'X'],
     10: ['Q', 'Z'] 
}

d_ru = {
    1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
     2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
     3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
     4: ['F', 'H', 'V', 'W', 'Y'],
     5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
     8: ['Ш', 'Э', 'Ю'],
     10: ['Ф', 'Щ', 'Ъ'] 
}

print("Введите слово : ")
word = input()

bank = 0

if ord(word[0]) > 122:
    print("Русское слово")
    for i in range(len(word)):
        for key in d_ru.keys():
            if d_ru[key].count(word[i].upper()):
                bank += key
else:
    print("Английское слово")
    for i in range(len(word)):
        for key in d_en.keys():
            if d_en[key].count(word[i].upper()):
                bank += key
         
print(f"Всего получено {bank} очков")




