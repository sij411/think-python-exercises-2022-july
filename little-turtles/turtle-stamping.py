import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
wn.bgcolor("lightgreen")
alex.shape("turtle")
alex.color("blue")

alex.penup()
size = 20

for i in range(30):
    alex.stamp()
    size += 3
    alex.forward(size)
    alex.right(24)

#to identify the real turtle as a instance
alex.color("red")
#As I expected, the last one is real turtle, a instance that python has.
wn.mainloop()