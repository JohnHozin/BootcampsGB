from random import randint
left = 0
rigth = 100000000
x = randint(left, rigth)

# метод последовательного перебора
# count = 0
# for i in range(0, 101):
#     count += 1
#     if i == x:
#         print("Число найдено!")
#         break
# print("Загаданное число", x, "найдено за ", count, " итераций, методом 1")


# метод угадайки
# count = 1
# y = randint(0, 100)
# while x != y:
#     y = randint(0, 100)
#     count += 1
# print("Загаданное число", x, "найдено за ", count, " итераций, методом 2")


# #метод угадывания пользователем
# count=1
# print("Угадай число от 0 до 100")
# y=int(input("Введите число "))
# while x != y:
#     if x<y: print("Искомое число меньше")
#     else: print("Искомое число больше")
#     y=int(input("Введите число "))
#     count += 1
# print("Загаданное число", x, "найдено за ", count, " итераций, методом 3" )


# метод угадывания компом
count = 1
y = (rigth+1 + left-1) // 2
while x != y:
    if x < y:
        rigth = y
    else:
        left = y
    y = int((rigth + left) / 2)
    count += 1
print("Загаданное число", x, "найдено за ", count, " итераций, методом 4")
