import turtle
import random

# Set up the racecourse
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Race Game")

# Create turtle racers
num_turtles = 5
turtles = []

# Define some recognized color names for turtles
colors = ["red", "green", "blue", "orange", "purple"]

for i in range(num_turtles):
    turtles.append(turtle.Turtle())
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-200, -20 * i)

# Function to move each turtle forward a random distance
def move_turtle(t):
    distance = random.randint(1, 20)
    t.forward(distance)

# Simulate the race
winner = None
while not winner:
    for t in turtles:
        move_turtle(t)
        if t.xcor() >= 200:
            winner = t.color()[0]

# Declare the winner
wn.title("Winner: " + winner)
t = turtle.Turtle()
t.penup()
t.goto(-50, 0)
t.write("Winner is " + winner, align="center", font=("Arial", 20, "bold"))
t.hideturtle()

wn.exitonclick()
