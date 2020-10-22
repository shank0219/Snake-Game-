import turtle
import time

delay=0.1

score=0
high_score=0

# 1 creating a background
bg=turtle.Screen()
bg.title('Welcome to Snake Game')
bg.bgcolor('black')
bg.setup(width=600, height=600)
bg.tracer(0)

# 2 creating a head
head=turtle.Turtle()
head.speed(8)
head.shape('square')
head.color('red')
head.penup()
import random as r
q=r.randrange(250)
p=r.randrange(250)
head.goto(q,p)
head.direction='stop'

# moving the head
def go_up():
    head.direction='up'
def go_down():
    head.direction='down'
def go_left():
    head.direction='left'
def go_right():
    head.direction='right'
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+10)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-10)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+10)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-10)

# Keyboard connections
bg.listen()
bg.onkeypress(go_up,'w')
bg.onkeypress(go_down,'s')
bg.onkeypress(go_left,'a')
bg.onkeypress(go_right,'d')

# Snake food
food=turtle.Turtle()
food.speed(5)
food.shape('square')
food.color('white')
food.penup()
import random as r
q=r.randrange(250)
p=r.randrange(250)
food.goto(q,p)

bits = []

# Scoring
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,-260)
pen.write('Score:0  High score:0', align='center', font=('Courier',24,'normal'))
pen.goto(0,-290)
pen.write('done by - gamer',align='right')
while True:
    bg.update()

    # Snake interaction with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(q,p)
        head.direction = 'stop'
        for bit in bits:
            bit.goto(1000,1000)
        # Clearing the bits
        bits.clear()

        #Scoring
        score=0
        pen.clear()
        pen.write('Score: {}  High score: {}'.format(score,high_score),align='center', font=('Courier',24,'normal'))



    if head.distance(food)<20:
        x= r.randint(-250,250)
        y= r.randint(-250,250)
        food.goto(x,y)
        # Adding a new segment
        new_bit=turtle.Turtle()
        new_bit.speed(0)
        new_bit.shape('square')
        new_bit.color('green')
        new_bit.penup()
        bits.append(new_bit)

        #Scoring
        score+=1
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write('Score: {}  High score: {}'.format(score,high_score),align='center', font=('Courier',24,'normal'))

        # For joining the bits to the snake Head
    for index in range(len(bits)-1,0,-1):
        x=bits[index-1].xcor()
        y=bits[index-1].ycor()
        bits[index].goto(x,y)

    if len(bits)>0:
        x=head.xcor()
        y=head.ycor()
        bits[0].goto(x,y)

    move()

    for bit in bits:
        if bit.distance(head) < 7:
            time.sleep(1)
            head.goto(q, p)
            head.direction = 'stop'
            score = 0
            pen.clear()
            pen.write('Score: {}  High score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))
            pen.write('done by - shashank,chethan,abhishek', align='right')
            for bit in bits:
                bit.goto(1000, 1000)

            # Clearing the bits

            bits.clear()


    time.sleep(delay)
bg.mainloop()
