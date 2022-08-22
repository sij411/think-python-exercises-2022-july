import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
wn.bgcolor("lightgreen")
#alex.hideturtle()
alex.shape("turtle")
alex.color("blue")


#11 
#for i in range(5):
    #alex.left(145)
    #alex.forward(100)

#12 

degree = 0

for i in range(12):
    alex.penup()
    alex.right(degree)
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(30)
    alex.stamp()
    alex.forward(-140)
    alex.left(degree)
    degree += 30
    
#뭐지? 코드 순서만 바꿨는데 갑자기 성공함
#핵심은 우측으로 돈 만큼 좌측으로 돌려 각도를 0으로 원상복귀한 것임. 



wn.mainloop()