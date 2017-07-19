from turtle import *
import math

# Name your Turtle.
Dell = Turtle()
# Set Up your screen and starting position.
setup(500,500)



### Write your code below:


sides = int(input("How many sides"))
for x in range(sides):
	Dell.left(360/sides)
	Dell.forward(150)
fillcolor(blue)
begin_fill(blue)
end_fill(blue)
# Close window on click.
exitonclick()