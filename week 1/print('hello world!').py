import turtle


screen = turtle.Screen()
screen.bgcolor("white")  

pen = turtle.Turtle()
pen.color("black") 
pen.pensize(2)     


def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144) 


draw_star(100)

pen.hideturtle()
turtle.done()

# introduce variable in program