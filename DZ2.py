#Задача 10

print("Введите количество монеток : ")
n = int(input())

count = 0

print("Введите стороны  (0 - решка, 1 - орел)")
    
for i in range(n):
    i = int(input())
    if i == 0:
        count += 1
    
print(f"{count} монеток нужно перевернуть")
        
#Задача 12

print("Введиче сумму : ")
s = int(input())

print("Введиче произведение : ")
p = int(input())

result = []

for i in range(s):
    if i == (s*i - p)**0.5:
        result.append(i)
               
if len(result) == 2:
    print(f"X = {result[0]}\nY = {result[1]}")
else: 
    print(f"X = {result[0]}\nY = {result[0]}")
    
            