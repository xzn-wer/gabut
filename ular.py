import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

# creating the window and setting width and height
wn = turtle.Screen()
wn.title("game ular asal asalan")
wn.bgcolor('black')
wn.setup(width=700, height=700)
wn.tracer(0)

# creating border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color('black')
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.penup()
border.hideturtle()

# creating head snake
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# creating food
food = turtle.Turtle()
food_color = random.choice(["yellow", "green", "tomato"])
food_shape = random.choice(["triangle", "square", "circle"])
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(20, 20)

# creating space to show score and high score
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape('square')
scoreBoard.color('white')
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 250)
scoreBoard.write("score : 0  high score : 0", align="center", 
                font=('courier', 25, "bold"))

# assigning key direction
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != 'right':
        head.direction = "left"

def move_right():
    if head.direction != 'left':
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
wn.listen()
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")

segments = []

# main game loop
while True:
    wn.update()

    # check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments of the body
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # reset the score
        score = 0
        scoreBoard.clear()
        scoreBoard.write("score : {} high score : {}".format(score, high_score), align="center", font=("courier", 25, "bold"))

    # check for collision with the food
    if head.distance(food) < 20:
        # increasing score and high score
        score += 10
        if score > high_score:
            high_score = score
        scoreBoard.clear()
        scoreBoard.write("score : {} high score : {}".format(score, high_score), align="center", font=("courier", 25, "bold"))

        # creating food at random location
        x_cord = random.randint(-290, 270)
        y_cord = random.randint(-240, 240)
        food_color = random.choice(["yellow", "green", "tomato"])
        food_shape = random.choice(["triangle", "square", "circle"])
        food.speed(0)
        food.shape(food_shape)
        food.color(food_color)
        food.goto(x_cord, y_cord)

        # adding new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white smoke")  # giving a new color to the tail
        new_segment.penup()
        segments.append(new_segment)  # adding new segment to the list

    # moving the snake and ending the game on collision of head with body segment
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    # checking for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            scoreBoard.goto(0, 0)
            scoreBoard.write("\t\tawokawokawok kalah\n score kamu adalah : {}".format(score), align="center", font=("courier", 30, "bold"))

    time.sleep(delay)
