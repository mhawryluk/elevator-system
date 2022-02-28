from elevator import Elevator
from direction import Direction


class ElevatorSystem:
    def __init__(self, elevator_count=4):
        self.elevators = [Elevator(i) for i in range(elevator_count)]

    def __str__(self):
        return '\n'.join(map(str, self.elevators))

    def pickup(self, floor, direction):
        elevator_pick = min(
            self.elevators, key=lambda elevator: elevator.get_destination_count())

        elevator_pick.add_destination(floor)

    def choose_floor(self, elevatorId, floor):
        self.elevators[elevatorId].add_destination(floor)

    def step(self):
        for elevator in self.elevators:
            elevator.move()

    def get_open_doors(self, floor):
        open_elevators = set()

        for elevator in self.elevators:
            if elevator.current_floor == floor and elevator.open_doors:
                open_elevators.add(elevator.id)

        return open_elevators

    def get_status(self):
        return [elevator.get_status() for elevator in self.elevators]
