
#Exercises
#1
for i in range(10):
    print("We like Python's turtles!")

#2
# cellphone obj에 attr과 method를 주다니 어떻게?

#3 
for i in ["Jan", "Feb", "Mar"]:
    print("One of the months of the year is ", i)
#4
#Answer is 45 degree because she turns 360... 360*10 = 3600 so, after 10 turns she returns to zero, the startline. 
#5 

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("#5-a")
for j in xs:
    print(j)

print("#5-b")
for k in xs:
    print(k, k**2, end=" ")
    print()

print("#5-c")
total = 0

for h in xs:
    total += h
print(total)

print("#5-d")
product = 1
for g in xs:
    product *= g
print(product)


#6 

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(3):
    alex.forward(80)
    alex.left(120)
    
alex.color("orchid")

for i in range(4):
    alex.forward(50)
    alex.left(90)

alex.color("red")

for i in range(6):
    alex.forward(50)
    alex.left(60)
    
alex.color("Royalblue")

for i in range(8):
    alex.forward(50)
    alex.left(45)

alex.color("HotPink")

#7
for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.forward(100)
    alex.left(i)  
    
#11
alex.color("green")
turtle.position()
for i in range(5):
    alex.forward(60)            
    alex.left(30)
        
wn.mainloop()