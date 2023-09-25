#1

a = int(input())
first = a // 1000
second = a // 100 - (a // 1000 * 10)
third = (a % 100 - a % 10) / 10
last = a % 10
if first + last == second - third:
    print('ДА')
else:
    print('НЕТ')

#2
age = int(input())

if age >= 18:
    print('Access is allowed')
else:
    print('Access denied')

#3
a = int(input())
b = int(input())
c = int(input())

if b - a == c - b:
    print('YES')
else:
    print('NO')

#4
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

#5
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1:
    print('YES')
else:
    print('NO')

#6
a, b, c = int(input()), int(input()), int(input())

if c < a < b or b < a < c:
    print(a)
elif c < b < a or a < b < c:
    print(b)
else:
    print(c)

#7
m = int(input())
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print(31)
elif m == 4 or m == 6 or m == 9 or m == 11:
    print(30)
else:
    print(28)

#8
weight = int(input())

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

#9
password, repassword = input(), input()

if password == repassword:
    print("Пароль принят")
else:
    print("Пароль не принят")

#10
n = int(input())

if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

#11
a, b = int(input()), int(input())

if a < b:
    print(a)
else:
    print(b)

#12
age = int(input())

if age <= 13:
    print('детство')
if 13 < age < 25:
    print('молодость')
if 24 < age < 59:
    print('зрелость')
if age > 59:
    print('старость')

#13
n, k, b = int(input()), int(input()), int(input())

if n == k == b:
    print('Равносторонний')
elif n == k != b or n == b != k or b == k != n:
    print('Равнобедренный')
else:
    print('Разносторонний')