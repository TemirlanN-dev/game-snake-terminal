'''
This is the system behind the game.
It is responsible for every object and mechanic in the game.

Using a matrix as the board and a set of coordinates for the snake's body.
'''
from Snake import Snake
from Food import Food
import msvcrt
import time

# Directions as coordinates 
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

class System:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)], up)
        self.apple = Food(0)

    # Creates a matrix based on given width and height
    def board(self): 
        board1 = []
        for i in range(self.height):
            board1.append([])
            for j in range(self.width):
                board1[i].append(" ")

        return board1

    # Prints out to the terminal
    def render(self): 
        apple_loc = self.apple.spawn() # Places an apple in a random location

        s = input("The controls are: wasd\nPress 'Enter' to start the game!")

        if s == "":
            while True:
                # Initializes the board every loop
                board = self.board() 

                # Renders the food
                board[apple_loc[1]][apple_loc[0]] = "⨂"

                # Renders the snake
                for i in self.snake.body:
                    board[i[1]][i[0]] = "◉"
                
                head = self.snake.getHead()
                board[head[1]][head[0]] = "▣"

                # Renders the adjusted board with borders
                print("+" + " -"*len(board[0]) + " +")
                for row in board:
                    print("|", *row, "|")
                print("+" + " -"*len(board[0]) + " +")

                # Moves the snake if no input is read
                time.sleep(0.4)
                self.snake.slither(self.snake.direction, apple_loc)

                # Checks if there is input
                if msvcrt.kbhit():
                    ans = msvcrt.getwch() # Moves in the direction based on input

                    if ans == "w":
                        self.snake.setDirection(up)
                        self.snake.slither(up, apple_loc)
                    elif ans == "d":
                        self.snake.setDirection(right)
                        self.snake.slither(right, apple_loc)
                    elif ans == "s":
                        self.snake.setDirection(down)
                        self.snake.slither(down, apple_loc)
                    elif ans == "a":
                        self.snake.setDirection(left)
                        self.snake.slither(left, apple_loc)
                    else:
                        break
                    
                
                # Ends game if collision detected based on the marker 'X'
                if "X" in self.snake.body: 
                    print("You scored: " + str(self.apple.get_score()) + " points!")
                    break
                
                # Sets a new location for the apple and updates score if apple is detected based on the marker 'F'
                if "F" in self.snake.body:
                    self.snake.body.remove("F")
                    apple_loc = self.apple.spawn()
                    self.apple.plus_score()

    
        





           

