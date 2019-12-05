import sys
from parking_lot_components import (ParkingLot, create_parking_lot, park_car, car_departure,
                       lot_status, car_by_colour, slot_by_car_number, slot_by_colour)


def executeCommand(parkingLot, command):
    if command[0] == 'create_parking_lot':
        parkingLot = create_parking_lot(command[1])
    elif command[0] == 'park':
        print(park_car(parkingLot, command[1], command[2]))
    elif command[0] == 'leave':
        print(car_departure(parkingLot, command[1]))
    elif command[0] == 'status':
        print(lot_status(parkingLot).rstrip('\n'))
    elif command[0] == 'slot_number_for_registration_number':
        print(slot_by_car_number(parkingLot, command[1]).rstrip(', '))
    elif command[0] == 'registration_numbers_for_cars_with_colour':
        print(car_by_colour(parkingLot, command[1]).rstrip(', '))
    elif command[0] == 'slot_numbers_for_cars_with_colour':
        print(slot_by_colour(parkingLot, command[1]).rstrip(', '))
    else:
        print('Command is not applicable')
    return parkingLot


def commandMode(parkingLot):
    try:
        command = input().split()
        while command[0] != 'exit':
            parkingLot = executeCommand(parkingLot, command)
            command = input().split()
    except Exception as e:
        print(e)


def fileReaderMode(parkingLot, fileName):
    try:
        with open(fileName) as file:
            commands = file.readlines()
            for command in commands:
                parkingLot = executeCommand(
                    parkingLot, command.replace('\n', '').split())
    except Exception as e:
        print(e)


def main():
    parkingLot = None
    if len(sys.argv) > 1:
        fileReaderMode(parkingLot, sys.argv[1])
    else:
        commandMode(parkingLot)


if __name__ == '__main__':
    main()