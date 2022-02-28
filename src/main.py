from elevatorsystem import ElevatorSystem


def text_simulation():

    def pickup():
        try:
            floor, direction = map(int, input(
                "<floor>, <direction>: ").split(','))
            elevator_system.pickup(floor, direction)
            pickups.add(floor)
            print(elevator_system)
        except ValueError:
            print('Wrong input')

    def step():
        nonlocal pickups
        
        elevator_system.step()
        print(elevator_system)

        picked_up_floors = set()

        for floor in pickups:
            open_doors = elevator_system.get_open_doors(floor)
            if open_doors:
                try:
                    chosen_floor = int(
                        input(f'floor #{floor} elevator\'s door open, choose floor: '))
                    elevator_system.choose_floor(
                        open_doors.pop(), floor, chosen_floor)
                    picked_up_floors.add(floor)
                    print(elevator_system)
                except ValueError:
                    print('Wrong input')

        pickups -= picked_up_floors


    elevator_count = int(input("number of elevators: "))
    elevator_system = ElevatorSystem(elevator_count)
    pickups = set()

    print('''----------

Type one of the following actions:

step -> make one step of the simulation

pickup -> the program will prompt you to enter the floor number and the direction of the pickup seperated by a comma!
the direction should be input as an integer - a positive number meaning UP and negative meaning DOWN
the prompt to choose floor destination when entering the elevator will come up once the elevator reaches the pickup floor and the directions match

exit -> terminate the program

----------
''')

    print(elevator_system)

    while True:
        action = input('>> ').strip()

        if action == 'pickup':
            pickup()
        elif action == 'step':
            step()
        elif action == 'exit':
            break
        else:
            print('Unrecognized action:', action)


if __name__ == '__main__':
    text_simulation()
