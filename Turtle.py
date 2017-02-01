"""Create a Turtle Program that will draw a 3-dimensional cube"""





"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
#This file can be seen in my MyFile.py file and it is pasted here
import turtle
LogansTurtle = turtle.Turtle()
def DrawRectangle(Anyturtle, l, w):
    for x in range(4):
        Anyturtle.forward(12)
        Anyturtle.right(90)
        Anyturtle.forward(w)
DrawRectangle(LogansTurtle, 4, 4)
print(DrawRectangle(Anyturtle, l, w))
