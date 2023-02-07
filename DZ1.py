#Задача 2

print("Введите трехзначное число : ")
a = input()

sum = int(a[0]) + int(a[1]) + int(a[2])

print(sum)

#Задача 4

print("Введите S: ")

s = int(input())
 
#6 = 1 = 1 = 4
#p == s
#k == 2*(p+s)

k = s/3*2
p = s = k/4

print(f"Катя : {k}\n Петя : {p}\nСережа : {s}")

#Задача 6

print("Введите номер билета (6 цифр) : ")
b = input()

if(int(b[0]) + int(b[1]) + int(b[2]) == int(b[3]) + int(b[4]) + int(b[5])):
    print("YES")
else:
    print("NO")
    
# Задача 8

print("Введите n : ")
n = int(input())
print("Введите m : ")
m = int(input())

s = n*m

print("Введите количество долек : ")
k = int(input())

if(k//n or k//m):
    print("YES")
else:
    print("NO")