from direction import Direction


class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.destinations = []
        self.open_doors = False

    def move(self):
        self.open_doors = False
        direction = self.get_direction()
        self.current_floor += direction.value

        while self.destinations and self.current_floor == self.destinations[0]:
            self.open_doors = True
            self.destinations.pop(0)

    def get_direction(self):
        if not self.destinations:
            return Direction.STAY
        if self.destinations[0] > self.current_floor:
            return Direction.UP
        if self.destinations[0] < self.current_floor:
            return Direction.DOWN
        return Direction.STAY

    def update(self, current_floor, destination):
        self.current_floor = current_floor
        self.destination = destination

    def get_status(self):
        return self.id, self.current_floor, self.destinations

    def get_destination_count(self):
        return len(self.destinations)

    def add_destination(self, floor):
        self.destinations.append(floor)
