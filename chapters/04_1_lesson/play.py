import turtle
import time
dee = turtle.Turtle()
dee.shape('turtle')
dee.color('red', 'green')
print(dee)

def animate_write(t, text):
    screen = turtle.Screen()
    screen.tracer(0, 0)
    partial_text = ''
    for c in text:
        partial_text += c
        t.clear()
        t.penup()
        t.goto(-200, -100)
        t.write(partial_text, font=("Chiller", 50, "normal"), align="center")
        screen.update()
        time.sleep(0.3)
writer = turtle.Turtle()
animate_write(writer, "Howdy")



turtle.mainloop()
