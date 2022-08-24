import turtle

def make_window(colr, ttle):
    """Set up the window with the given bground color and title.
    Returns the new window. 

    Args:
        colr (str): window bgcolor
        ttle (str): title of window
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """Set up a turtle with the given color and pensize.
    Returns the new turtle.

    Args:
        colr (str): color of turtle
        sz (int): pensize
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)
     
     
wn.mainloop()