# Responsible for every mechanic that the snake object would need

class Snake:
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    # Updates the coordinate of the head to a new one based on the direction
    def slither(self, new_direction, apple_pos):
        newPos = tuple(map(sum,zip(self.getHead(), new_direction))) 

        # Adds a marker if collides with the border
        if newPos[0] >= 15 or newPos[1] >= 15: 
            self.body.append("X")
        elif newPos[0] < 0 or newPos[1] < 0:
            self.body.append("X")

        # Adds a marker if it tries to move where it already exists
        if newPos in self.body: 
            self.body.append("X")
        else:
            self.body.pop(0)
            self.body.append(newPos)

        # Adds a marker if it collides with a food object
        if newPos == apple_pos:
            self.body.append(newPos)
            self.body.insert(0, "F")

    # Updates direction 
    def setDirection(self, newDirection):
        self.direction = newDirection

    # Returns the coordinate of the head of the snake
    def getHead(self):
        return self.body[-1]
    


