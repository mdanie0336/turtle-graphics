import random
from turtle import *

myles = Turtle()
salem = Turtle()
xan = Turtle()

myles.shape("turtle")
myles.color("blue")

salem.shape("turtle")
salem.color("purple")

xan.shape("turtle")
xan.color("green")

xan.forward(50)

for i in range(10):
    xan.left(53)
    myles.right(36)
    xan.forward(11)
    myles.forward(50)

salem.left(90)

all_turtles = [myles, salem, xan]

while True:
    for t in all_turtles:
        rand_dir = random. randint(-20,20)
        rand_dist = random.randint(5,10)

        t.right(rand_dir)
        t.forward(rand_dist)
    
