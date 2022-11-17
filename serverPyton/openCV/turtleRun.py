from turtle import *
from random import randint
import time

finish = 200  # дистанция гонки

t1 = Turtle()  # создали объект
t1.shape("turtle")  # поменяли форму
t1.color("red")  # поменяли цвет
t1.penup()  # поднимаем черепашку чтобы не рисовала
t1.goto(-200, 20)  # перемещаем черепашку по координатам
t1.pendown()  # опускаем черепашку чтобы потом рисовала

t2 = Turtle()  # создали объект
t2.shape("turtle")  # поменяли форму
t2.color("blue")  # поменяли цвет
t2.penup()  # поднимаем черепашку чтобы не рисовала
t2.goto(-200, -20)  # перемещаем черепашку по координатам
t2.pendown()  # опускаем черепашку чтобы потом рисовала


def razmetka():  # функция рисует разметку поля
    t = Turtle()  
    t.speed(0)  
    for i in range(1,21):  
        t.penup()  
        t.goto(-200 + i * 20, 50)
        t.pendown()
        t.goto(-200 + i * 20, -50)
    t.hideturtle()

razmetka()

while t1.xcor() < finish and t2.xcor() < finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))

time.sleep(5)  # задержка
