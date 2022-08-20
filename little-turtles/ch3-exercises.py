
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