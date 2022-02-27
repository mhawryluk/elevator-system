from elevatorsystem import ElevatorSystem


elevator_count = int(input("number of elevators: "))
elevator_system = ElevatorSystem(elevator_count)

pickups = []

while True:

    action = input()

    if action == 'pickup':
        floor, direction = map(int, input("floor, direction").split(','))
        elevator_system.pickup(floor, direction)
        pickups.append(floor)

    elif action == 'step':
        elevator_system.step()
        print(elevator_system.get_status())

        for floor in pickups:
            open_doors = elevator_system.get_open_doors(floor)
            if open_doors:
                chosen_floor = int(
                    input(f'floor #{floor} elevator\'s door open, choose floor'))
                elevator_system.choose_floor(open_doors[0], chosen_floor)
