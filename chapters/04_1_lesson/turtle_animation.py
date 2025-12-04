import turtle
import time
import random

screen = turtle.Screen()
turtle.tracer(False)

turtles: list[turtle.Turtle] = []

def add_turtle(x, y):
    global turtles
    t = turtle.Turtle()
    turtle.colormode(255)
    t.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.shape('turtle')
    turtles.append(t)

screen.onclick(add_turtle)

X_BOUND = 300
Y_BOUND = 300


while True:
    for t in turtles:
        (old_x, old_y) = t.position()
        possible_moves = [t.forward, t.back, t.right, t.left]
        random_value = random.randint(0, 100)
        random.choice(possible_moves)(random_value)
        (new_x, new_y) = t.position()
        if (new_x > X_BOUND or new_y < -X_BOUND or new_y > Y_BOUND or new_y < -Y_BOUND):
            t.goto(old_x, old_y)
    time.sleep(0.05)
    screen.update()

turtle.mainloop()