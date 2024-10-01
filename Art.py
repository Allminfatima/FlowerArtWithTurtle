import turtle
import random

# Set up the turtle environment
turtle.bgcolor("black")  # Background color
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Set the width of the turtle pen

# Function to draw a petal
def draw_petal():
    t.color(random.random(), random.random(), random.random())  # Random petal color
    t.begin_fill()
    for _ in range(2):
        t.circle(100, 60)  # Draw half of the petal
        t.left(120)        # Draw the other half of the petal
        t.circle(100, 60)
        t.left(120)
    t.end_fill()

# Function to draw a flower
def draw_flower():
    for _ in range(12):  # Number of petals
        draw_petal()       # Draw a petal
        t.right(30)        # Rotate to position for the next petal

# Function to draw the center of the flower
def draw_center():
    t.penup()
    t.goto(0, -20)  # Move to the center position
    t.pendown()
    
    # Draw the yellow center
    t.color("yellow")  # Center color
    t.begin_fill()
    t.circle(20)  # Draw the center circle
    t.end_fill()

    # Draw the brown dot in the center
    t.penup()
    t.goto(0, -10)  # Position for the brown dot
    t.pendown()
    t.color("brown")  # Dot color
    t.begin_fill()
    t.circle(10)  # Draw the brown dot
    t.end_fill()

# Function to draw the stem
def draw_stem():
    t.penup()
    t.goto(0, -20)  # Start from the center of the flower
    t.setheading(270)  # Point downwards
    t.pendown()
    t.color("green")  # Stem color
    t.begin_fill()
    t.pensize(10)  # Thicker stem
    t.forward(150)  # Draw the stem
    t.end_fill()

# Function to draw a leaf
def draw_leaf():
    t.color("lightgreen")  # Leaf color
    t.begin_fill()
    t.circle(30, 90)  # Draw the first half of the leaf
    t.left(90)        # Turn to draw the second half of the leaf
    t.circle(30, 90)  # Complete the leaf shape
    t.end_fill()
    t.right(90)       # Reset the turtle orientation

# Function to add leaves to the stem
def draw_leaves():
    t.penup()
    t.goto(0, -120)  # Position leaves on the stem
    t.pendown()
    t.setheading(160)  # Angle for the first leaf
    draw_leaf()        # Draw the first leaf

    t.penup()
    t.goto(0, -120)  # Move back to the stem for the second leaf
    t.pendown()
    t.setheading(290)   # Angle for the second leaf
    draw_leaf()        # Draw the second leaf

# Draw the flower, center, stem, and leaves
draw_flower()
draw_center()
draw_stem()
draw_leaves()

# Hide the turtle and finish
t.hideturtle()
turtle.done()
