import turtle
  
  
def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""  #Docstring
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
    
    
wn = turtle.Screen() #윈도우창 소환식
wn.bgcolor("lightgreen") #윈도우 꾸미기. 윈꾸

tess = turtle.Turtle() #거북이 소환식
tess.pensize(3) #거북이 근성장

tess.speed(0)#0이 젤 fatest

size = 20
for i in range(30):
    draw_multicolor_square(tess, size)
    size += 10
    tess.forward(10)
    tess.right(18)
    

wn.mainloop()
  
  
