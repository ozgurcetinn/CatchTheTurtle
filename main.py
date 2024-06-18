import turtle
import random
import time

#create screen
screen = turtle.Screen()
screen.bgcolor("light blue")

#Create Timer

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 260)  #Position the timer
timer.color("black")
timer.write("Time remain for Shredder", align="center", font=("Arial", 16, "normal"))

# Create score
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(0, 220) #position score_table
score_board.color("black")
score_board.write("Score: 0", align="center", font=("Arial", 16, "normal"))

# Create Ninja Turtle Leonardo
leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.penup()
leonardo.speed("fastest")

#setting our variables
score = 0
duration = 20
start_time = time.time()

def leonardo_position():
    """put leonardo on a random area that include with (x:-200,200 and y:-200,180"""
    leonardo.goto(random.randint(-200, 200), random.randint(-200, 180)) #because of score board its a bit lower y+=180

def leonardo_find(x, y):
    """relocate leonardo position, increase score and we will use it with onclick function"""
    global score
    if leonardo.distance(x, y) < 10:
        score += 1
        score_board.clear()
        score_board.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
        print(f"Score: {score}")
        leonardo_position()

screen.onclick(leonardo_find)

while (time.time() - start_time) < duration:
    leonardo_position()
    time.sleep(0.55)

    # Update timer
    time_remain = int(duration - (time.time() - start_time))
    timer.clear()
    timer.write(f"Time remain for Shredder: {time_remain}", align="center", font=("Arial", 16, "normal"))

leonardo_position()

timer.clear()
timer.goto(0, 0)
timer.write(f"Game Over\nFinal Score: {score}", align="center", font=("Arial", 24, "normal"))

score_board.clear()

turtle.mainloop()
