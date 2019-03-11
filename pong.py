#!/usr/local/bin/python

import turtle
import os
import time

every_other = True
paused = True
boing = "./cartoon_boing.wav&"
score = "./power_up.wav&"
win = "./win.wav&"
wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)
paddleA.clear

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)
paddleB.clear

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddleA_Up():
    y = paddleA.ycor()
    if (y + 50) <= 300:
         y += 30
         paddleA.sety(y)

def paddleA_Down():
    y = paddleA.ycor()
    if (y - 50) >= -300:
         y -= 30
         paddleA.sety(y)

def paddleB_Up():
    y = paddleB.ycor()
    if (y + 50) <= 300:
         y += 30
         paddleB.sety(y)

def paddleB_Down():
    y = paddleB.ycor()
    if (y - 50) >= -300:
         y -= 30
         paddleB.sety(y)

def Close():
    wn.bye()

def winner( a, b ):
    winner = getWinner(a, b)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.penup()
    pen.hideturtle()
    pen.write(winner + "  Wins!", align="center", font=("Courier", 72, "normal"))
    os.system("afplay " + win)
    if timer():
        pen.clear()
        paddleB.goto(350, 0)
        paddleA.goto(-350, 0)

def timer():
    mins = 0
    while mins != 0.05:
        time.sleep(3)
        mins += .05
    return True

def getWinner( a, b ):
    if (a > b):
        return "Player A"
    else:
        return "Player B"

def pause():
    time.sleep(5)

# Key Binding
wn.onkey(Close, "Escape")
wn.onkey(paddleA_Up, "w")
wn.onkey(paddleA_Down, "s")
wn.onkey(paddleB_Up, "Up")
wn.onkey(paddleB_Down, "Down")
wn.onkey(pause, "space")
wn.listen()

# Main Game Loop
while True:
    wn.update()

    # Entry point pause
    if paused:
        pause()
        paused = False

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
        os.system("afplay " + boing)
        # afplay is MacOS command to play sound, the & prevents the game from pausing when starting the sound

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        os.system("afplay " + boing)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        if every_other:
            ball.dx *= -1
            every_other = False
        else:
            ball.dx *= -1
            ball.dy *= -1
            every_other = True
        os.system("afplay " + score)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        if score_a >= 5:
            ball.goto(0, 0)
            winner(score_a, score_b)
            score_a = 0
            score_b = 0
            pen.clear()
            pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        if every_other:
            ball.dx *= -1
            every_other = False
        else:
            ball.dx *= -1
            ball.dy *= -1
            every_other = True
        os.system("afplay " + score)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        if score_b >= 5:
            ball.goto(0, 0)
            winner(score_a, score_b)
            score_a = 0
            score_b = 0
            pen.clear()
            pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 49 and ball.ycor() > paddleB.ycor() - 49):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay " + boing)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 49 and ball.ycor() > paddleA.ycor() - 49):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay " + boing)
