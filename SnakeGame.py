from tkinter import *;
import random;

GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=250
SIZE=50
BODY=1
SNAKE_COLOR="#00FF00"
FOOD_COLOR="#FF0000"
BG_COLOR="#000000"


class Snake():
    def __init__(self):
        self.body_size=BODY
        self.coordinates=[]
        self.squares=[]
        
        for i in range(0,BODY):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SIZE, y+SIZE, fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)

class Food():
    def __init__(self):

        x=random.randint(0,int(GAME_WIDTH/SIZE)-1)* SIZE #700/50=14
        y=random.randint(0,int(GAME_HEIGHT/SIZE)-1)* SIZE

        self.coordinates=[x,y]

        canvas.create_oval(x, y, x+ SIZE, y+SIZE,fill=FOOD_COLOR, tag="food")



def Turn(snake, food):

    x,y=snake.coordinates[0]
    if direction=="up":
        y-=SIZE
    elif direction=="down":
        y+=SIZE
    elif direction=="left":
        x-=SIZE
    elif direction=="right":
        x+=SIZE
    
    snake.coordinates.insert(0,(x,y))

    square=canvas.create_rectangle(x,y,x+SIZE,y+SIZE,fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:

        global score

        score+=1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food= Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if collsions(snake):
        end_game()

    else:
        Window.after(SPEED,Turn,snake,food)




def change_direction(new_direction):
    
    global direction

    if new_direction=='left':
        if direction!='right':
            direction=new_direction
    elif new_direction=='right':
        if direction!='left':
            direction=new_direction
    elif new_direction=='up':
        if direction!='down':
            direction=new_direction
    elif new_direction=='down':
        if direction!='up':
            direction=new_direction

def collsions(snake):
    
    x,y=snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    
    for body in snake.coordinates[1:]:
        if x== body[0] and y== body[1]:
            return True
    

def end_game():
    
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Courier',70),text=" GAME OVER", fill="red", tag="gameover")

score=0
direction='down'

Window=Tk()
Window.title("🐍 Game")
Window.resizable(False,False)
label= Label(Window,text="Score:{}".format(score),font=('Helvetica',30))
label.pack()
canvas=Canvas(Window,background=BG_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
Window.update()

Window_width=Window.winfo_width()
Window_height=Window.winfo_height()
screen_width=Window.winfo_screenwidth()
screen_height=Window.winfo_screenheight()

x=int((screen_width/2)-(Window_width/2))
y=int((screen_height/2)-(Window_height/2))

Window.geometry(f"{Window_width}x{Window_height}+{x}+{y}")

Window.bind('<Left>', lambda event: change_direction('left'))

Window.bind('<Right>', lambda event: change_direction('right'))

Window.bind('<Up>', lambda event: change_direction('up'))

Window.bind('<Down>', lambda event: change_direction('down'))

snake= Snake()
food= Food()
Turn(snake,food)

Window.mainloop()
