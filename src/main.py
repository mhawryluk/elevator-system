from elevatorsystem import ElevatorSystem


def text_simulation():
    elevator_count = int(input("number of elevators: "))
    elevator_system = ElevatorSystem(elevator_count)
    print(elevator_system)

    pickups = set()

    while True:

        action = input('>> ')

        if action == 'pickup':
            try:
                floor, direction = map(int, input(
                    "floor, direction: ").split(','))
                elevator_system.pickup(floor, direction)
                pickups.add(floor)
                print(elevator_system)
            except ValueError:
                print('Wrong input')

        elif action == 'step':
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
                            open_doors.pop(), chosen_floor)
                        picked_up_floors.add(floor)
                        print(elevator_system)
                    except ValueError:
                        print('Wrong input')

            pickups -= picked_up_floors

        elif action == 'exit':
            break

        else:
            print('Unrecognized action:', action)


if __name__ == '__main__':
    text_simulation()
