
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lavender")
wn.title("Turtle turtle turtle")

alex = turtle.Turtle()
alex.pensize(3)
alex.color("hotpink")
#1: squares and void function

def make_mini_square(colr, n):
    """Drawing mini squares. Enter square's color and how many squares you want to draw.

    Args:
        colr (str): square's color, -> this arg assigns turtle's color.
        n (int): the number of square
    """
    alex.color(colr)
    for i in range(n):
        for j in range(4):
            alex.forward(20)
            alex.left(90)
        alex.penup()
        alex.forward(35)
        alex.pendown()

#make_mini_square("hotpink", 5)

  

#2 Squares are getting bigger!

size = 20

def make_bigger_square(n):
    """Drawing bigger and bigger squares.

    Args:
        n (int): the number of squares
    """
    size = 20
    diagonal = math.sqrt(800)
    for i in range(n):
        for j in range(4):
            alex.forward(size)
            alex.right(90)
        size += 20
        alex.penup()
        alex.left(135)
        alex.forward(diagonal)
        alex.right(135)
        alex.pendown()
        
        
    

make_bigger_square(5)






wn.mainloop()  