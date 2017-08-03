import turtle
import random

turtle.tracer(1,0)




SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape('square')

turtle.hideturtle()
#THE SNAKE'S BODY
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=snake.stamp()
    stamp_list.append(stamp1)
#SNAKE'S MOVEMENT
UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEO=100
SPACEBAR='space'

UP=0
LEFT=2
DOWN=1
RIGHT=3
direction=UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400
def up ():
    global direction
    direction=UP
    print('you pressed up')
def down():
    global direction
    direction=DOWN
    print('you pressed down')

def left():
    global direction
    direction=LEFT
    print('you pressed left')
def right():
    global direction
    direction=RIGHT
    print('you pressed right')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()
#make random food pop up
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    foodstampss=food.stamp()
    food_stamps.append(foodstampss)
        
#IDK SNAKE MOVEMENTS PART 2 I GUESS                 

def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if snake.pos() in pos_list[0:-1]:
        print('you committed suicide')
        quit()

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('YOU MOVED RIGHT!')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('YOU MOVED LEFT')
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('YOU MOVED UP')
    else:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('YOU MOVED DOWN')
        
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    global food_stamps,food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('fooooooooodddddd')
        print(len(pos_list))
        make_food()
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
    
    
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print('YOU ARE AN IDIOT, YOU LOST R')
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print('YOU ARE AN IDIOT, YOU LOST L')
        quit()
    elif new_y_pos >= UP_EDGE:
        print('YOU ARE AN IDIOT, YOU LOST U')
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print('YOU ARE AND IDIOT,YOU LOST D')
        quit()

    TIME_STEP=100
    turtle.ontimer(move_snake,TIME_STEP)
    
        


move_snake()
food=turtle.clone()
food.shape('turtle')
food_pos=[(100,100),(-100,-100)]
food_stamps=[]
food.hideturtle()

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    my_food_stamp=food.stamp()
    food_stamps.append(my_food_stamp)
#THE EDGES OF THE GAME(BORDERS)
turtle.goto(-400,250)
turtle.pendown()
turtle.goto(400,250)
turtle.goto(400,-250)
turtle.goto(-400,-250)
turtle.goto(-400,250)


turtle.mainloop()

