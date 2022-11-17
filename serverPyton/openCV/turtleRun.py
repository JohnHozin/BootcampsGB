from turtle import *
from random import randint
import time

finish = 400  # дистанция гонки

t1 = Turtle()  # создали объект
t1.shape("turtle")  # поменяли форму
t1.color("red")  # поменяли цвет
t1.penup()  # поднимаем черепашку чтобы не рисовала
t1.goto(-400, 20)  # перемещаем черепашку по координатам
t1.pendown()  # опускаем черепашку чтобы потом рисовала
t1.speed(3)

t2 = Turtle()  # создали объект
t2.shape("turtle")  # поменяли форму
t2.color("blue")  # поменяли цвет
t2.penup()  # поднимаем черепашку чтобы не рисовала
t2.goto(-400, -20)  # перемещаем черепашку по координатам
t2.pendown()  # опускаем черепашку чтобы потом рисовала
t2.speed(3)

t3 = Turtle()  # создали объект
t3.shape("turtle")  # поменяли форму
t3.color("green")  # поменяли цвет
t3.penup()  # поднимаем черепашку чтобы не рисовала
t3.goto(-400, -60)  # перемещаем черепашку по координатам
t3.pendown()  # опускаем черепашку чтобы потом рисовала
t3.speed(3)

t4 = Turtle()  # создали объект
t4.shape("turtle")  # поменяли форму
t4.color("yellow")  # поменяли цвет
t4.penup()  # поднимаем черепашку чтобы не рисовала
t4.goto(-400, 60)  # перемещаем черепашку по координатам
t4.pendown()  # опускаем черепашку чтобы потом рисовала
t4.speed(3)

def razmetka():  # функция рисует разметку поля
    t = Turtle()
    t.speed(0)
    for i in range(1, 41):
        t.penup()
        t.goto(-400 + i * 20, 80)
        t.pendown()
        t.goto(-400 + i * 20, -80)
    t.hideturtle()


razmetka()

def catch1(x, y):  # это обработчик события нажатия
    t1.write("Ouch!", font=("Arial", 14, "normal"))  # пишем на экране ауч
    t1.fd(randint(10, 15))  # черепашка делает случайный шаг от 10 до 15

t1.onclick(catch1)

def catch2(x, y):  # это обработчик события нажатия
    t2.write("Ouch!", font=("Arial", 14, "normal"))  # пишем на экране ауч
    t2.fd(randint(10, 15))  # черепашка делает случайный шаг от 10 до 15

t2.onclick(catch2)

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish and t4.xcor() < finish:
    t1.forward(randint(1, 7))
    t2.forward(randint(1, 7))
    t3.forward(randint(1, 7))
    t4.forward(randint(1, 7))
    #time.sleep(0.05)

#time.sleep(5)  # задержка
