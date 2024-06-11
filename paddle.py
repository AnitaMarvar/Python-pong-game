from turtle import Screen,Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()     #turtle ke saare features include hoge
       
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_len= 1, stretch_wid= 4)

        self.penup()
        self.goto(position)
        
    def go_up(self):        #methods mein pahele attribute hamesha self hi hota hai
        new_Y = self.ycor()+28
        self.goto(self.xcor(),new_Y)

    def go_down(self):
        new_Y = self.ycor()-28
        self.goto(self.xcor(),new_Y)

