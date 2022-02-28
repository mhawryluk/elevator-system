from direction import Direction


class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.destinations = set()
        self.direction = Direction.STAY
        self.open_doors = False

    def __str__(self):
        return f'| id: {self.id}, floor: {self.current_floor}, dest: {self.destinations}, dir: {self.direction.name}' + (', DOOR OPEN |' if self.open_doors else ' |')

    def move(self):
        self.open_doors = False
        self.current_floor += self.direction.value

        if self.current_floor in self.destinations:
            self.destinations.remove(self.current_floor)
            self.open_doors = True

        self.update_direction()

    def update_direction(self):
        if self.destinations and max(self.destinations) == min(self.destinations) == self.current_floor:
            self.direction = Direction.STAY
        elif self.destinations:
            if self.direction is Direction.DOWN:
                if min(self.destinations) > self.current_floor:
                    self.direction = Direction.UP
            elif self.direction is Direction.UP:
                if max(self.destinations) < self.current_floor:
                    self.direction = Direction.DOWN
            else:
                if max(self.destinations) > self.current_floor:
                    self.direction = Direction.UP
                else:
                    self.direction = Direction.DOWN

        else:
            self.direction = Direction.STAY

    def get_status(self):
        return self.id, self.current_floor, self.destinations

    def get_destination_count(self):
        return len(self.destinations)

    def add_destination(self, destination):
        self.destinations.add(destination)
        self.update_direction()
