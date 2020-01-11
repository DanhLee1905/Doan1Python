import turtle
import time
from tkinter import *

window=Tk()
window.geometry("300x300")
window.title("Control")

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Python clock 4")
wn.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(s,pen):

    #Man hinh clock
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    #Draw gio
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        
    #Draw kim giay
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s /60)* 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)



def Start():
    s = int (0)
    while TRUE:
        draw_clock(s,pen)
        wn.update()
        s += 1
        pen.clear()


def Sta():
    s = int (0)
    while TRUE:
        draw_clock(s,pen)
        wn.update()
        pen.clear()





b1 = Button (window,text="Start",width=12,bg='brown',fg='white',command=Start)
b1.place(x=1,y=1)

b2 = Button (window,text="Stop",width=12,bg='brown',fg='white', command=Sta)
b2.place(x=1,y=30)


window.mainloop()
wn.mainloop()