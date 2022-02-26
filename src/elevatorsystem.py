from elevator import Elevator
from direction import Direction


class ElevatorSystem:
    def __init__(self, elevator_count=4):
        self.elevators = [Elevator(i) for i in range(elevator_count)]

    def pickup(self, floor, direction):
        pass

    def step(self):
        for elevator in self.elevators:
            elevator.move()

    def get_status(self):
        return [elevator.get_status() for elevator in self.elevators]
