# Responsible to keep the score of the player as well as the spawn of the apple object
import random

class Food: 
    def __init__(self, score):
        self.score = score
        pass

    # Returns a random coordinate to put on the board
    def spawn(self): 
        x = random.randint(1, 14)
        y = random.randint(1, 14)
        return (x, y)
    
    # Updates score
    def plus_score(self): 
        self.score += 1

    # Returns score
    def get_score(self): 
        return self.score
