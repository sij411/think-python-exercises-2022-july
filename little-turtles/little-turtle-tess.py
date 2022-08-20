
bg_color = input("What bg-color do you want to change?:", )
tess_color = input("What color do you want to change?:", )
tess_size = int(input("What size?:", ))



import turtle
wn = turtle.Screen()



wn.bgcolor(bg_color)
wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color(tess_color)
tess.pensize(tess_size)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()

    # Extension !!!
    #