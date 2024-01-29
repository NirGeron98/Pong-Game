from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position, screen, up_key, down_key):
        super().__init__()
        
        self.screen = screen
        self.screen.tracer(0)
        self.speed(0)
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
       
        self.goto(position)

        # Set the delay for long presses
        self.delay = 50  # milliseconds

         # Initialize movement variables
        self.move_up_pressed = False
        self.move_down_pressed = False

        # Bind key press and release events
        self.screen.onkeypress(self.start_move_up, up_key)
        self.screen.onkeypress(self.start_move_down, down_key)
        self.screen.onkeyrelease(self.stop_move_up, up_key)
        self.screen.onkeyrelease(self.stop_move_down, down_key)

        # Enable listening to key events
        self.screen.listen()

        self.screen.update()

    def start_move_up(self):
        self.move_up_pressed = True
        self.move()


    def start_move_down(self):
        self.move_down_pressed = True
        self.move()

    def stop_move_up(self):
        self.move_up_pressed = False

    def stop_move_down(self):
        self.move_down_pressed = False

    def move(self):
        y = self.ycor()
        if self.move_up_pressed:
            if y < 210:
                y += 20
        elif self.move_down_pressed:
            if y > -210:
                y -= 20

        self.sety(y)


        self.screen.ontimer(lambda: self.move, self.delay)

