"""# AddTen(n):  Adds 10 to the parameter n and returns the result"""
def AddTen(n):
    n = n + 10
    return (n)
    print(AddTen(100))
"""# DrawRectangle(Anyturtle, l, w):  Self Explanitory"""
import turtle
LogansTurtle = turtle.Turtle()
def DrawRectangle(Anyturtle, l, w):
    for x in range(4):
        Anyturtle.forward(12)
        Anyturtle.right(90)
        Anyturtle.forward(w)
DrawRectangle(LogansTurtle, 4, 4)
print(DrawRectangle(Anyturtle, l, w))
 """# DrawPoly(Anyturtle, n):  Will draw a regular polygon with 'n' sides of"""
LogansTurtleV2 = turtle.Turtle()
def DrawPoly(Anyturtle, n):
    for you in range(2):
    Anyturtle.forward(20)
    Anyturtle.right(45)
    Anyturtle.forward(10)
    Anyturtle.right(90)
    Anyturtle.forward(10)
    Anyturtle.right(45)
print(DrawPoly)
