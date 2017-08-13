import turtle

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("white")
    angie.circle(100)

def draw_triangle():
    hey = turtle.Turtle()
    hey.shape("classic")
    hey.color("black")
    hey.forward(100) 
    hey.left(120)
    hey.forward(100)
    hey.left(120)
    hey.forward(100)

def draw_squares(brad):
    count = 0
    while(count < 4):
        if (count == 0):
            brad.shape("arrow")
            brad.color("yellow")
            brad.speed(3)
        elif (count == 2):
            brad.shape("turtle")
            brad.color("blue")
            brad.speed(3)
        elif (count == 3):
            brad.shape("circle")
            brad.color("green")
            brad.speed(3)
        else:
            brad.shape("triangle")
            brad.color("black")
            brad.speed(4)

        brad.forward(100)
        brad.right(90)
        count = count + 1

def draw_image():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()

    for i in range (1, 37):
         draw_squares(brad)
         brad.right(10)

    draw_circle()
    draw_triangle()

    window.exitonclick()

draw_image()


