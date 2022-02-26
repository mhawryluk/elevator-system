from direction import Direction


class Elevator:
    def __init__(self):
        self.current_floor = 0
        self.destination = 0

    def move(self):
        direction = self.get_direction()
        self.current_floor += direction

    def get_direction(self):
        if self.destination > self.current_floor:
            return Direction.UP
        elif self.destination < self.current_floor:
            return Direction.DOWN
        return Direction.STAY

    def update(self, current_floor, destination):
        self.current_floor = current_floor
        self.destination = destination
