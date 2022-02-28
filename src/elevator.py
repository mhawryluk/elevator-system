from direction import Direction


class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0

        self.up_destinations = set()
        self.down_destinations = set()

        self.direction = Direction.STAY
        self.open_doors = False

    def __str__(self):
        return f'| id: {self.id}, floor: {self.current_floor}, dest: {self.destinations()}, dir: {self.direction.name}' + (', DOOR OPEN |' if self.open_doors else ' |')

    def move(self):
        '''
            one simulation step,
            represents the journey from one floor the the closest neighboring one
        '''
        self.open_doors = False
        self.current_floor += self.direction.value
        self.check_open_doors()
        self.update_direction()

    def check_open_doors(self):
        '''
            checks if destination was reached
            and sets open_doors flag if so
        '''
        if not self.direction is Direction.UP and self.current_floor in self.down_destinations:
            self.down_destinations.remove(self.current_floor)
            self.open_doors = True
        if not self.direction is Direction.DOWN and self.current_floor in self.up_destinations:
            self.up_destinations.remove(self.current_floor)
            self.open_doors = True

    def update_direction(self):
        '''
            checks if it should go in the same direction
            or make a switch
        '''
        destinations = self.destinations()
        if destinations:
            if self.direction is Direction.UP and max(destinations) == self.current_floor: # reached the highest destination
                self.direction = Direction.STAY
                self.check_open_doors()
            elif self.direction is Direction.DOWN and min(destinations) == self.current_floor: # reached the lowest destination
                self.direction = Direction.STAY
                self.check_open_doors
            elif self.direction is Direction.DOWN:
                if min(destinations) >= self.current_floor: # no more floors to reach in the DOWN direction
                    self.direction = Direction.UP
            elif self.direction is Direction.UP:
                if max(destinations) <= self.current_floor: # no more floors to reach in the UP direction
                    self.direction = Direction.DOWN
            else: # wasn't moving, new destination appeared
                if max(destinations) > self.current_floor:
                    self.direction = Direction.UP
                else:
                    self.direction = Direction.DOWN

        else:
            self.direction = Direction.STAY

    def destinations(self):
        '''
            returns a shared set of destinations,
            including both directions
        '''
        return self.up_destinations | self.down_destinations

    def get_status(self):
        '''
            returns a tuple of essential information 
            on the elevator's current state
        '''
        return self.id, self.current_floor, self.destinations()

    def get_destination_count(self):
        '''
            used as metrics for choosing an elevator for pickup
        '''
        return len(self.destinations())

    def add_destination(self, destination, direction):
        '''
            used for pickup or choosing the destination floor inside the elevator
        '''
        if direction is Direction.UP:
            self.up_destinations.add(destination)
        elif direction is Direction.DOWN:
            self.down_destinations.add(destination)

        self.update_direction()
