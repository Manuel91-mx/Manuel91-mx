from random import randint
import readchar
import time
import os

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUMBER_OF_PIECES = 11

my_position = [6, 3]
map_object = []
tail_length = 0
tail = []

for numbers in range(NUMBER_OF_PIECES):
    random_x = randint(0, MAP_WIDTH)
    random_y = randint(0, MAP_HEIGHT)
    list_random = [random_x, random_y]

    if list_random in map_object:

        while list_random in map_object or list_random in my_position:
            random_x = randint(0, 19)
            random_y = randint(0, 14)
            list_random = [random_x, random_y]

        map_object.append(list_random)
    else:
        map_object.append(list_random)




while True:

    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_objects in map_object:

                if map_objects[POS_X] == coordinate_x and map_objects[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_objects

            for tail_piece in tail:

                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_object.remove(object_in_cell)
                    tail_length += 1
                    random_x = randint(0, MAP_WIDTH)
                    random_y = randint(0, MAP_HEIGHT)
                    list_random = [random_x, random_y]

                    if list_random in map_object:

                        while list_random in map_object or list_random in my_position:
                            random_x = randint(0, 19)
                            random_y = randint(0, 14)
                            list_random = [random_x, random_y]

                        map_object.append(list_random)
                    else:
                        map_object.append(list_random)

            print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * (MAP_WIDTH * 3) + "+")



    direction = readchar.readchar().decode()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break
    if my_position in tail[:tail_length]:
        print("Has chocado con tu cola, perdiste... :(")
        time.sleep(3)
        break

    os.system("cls")



