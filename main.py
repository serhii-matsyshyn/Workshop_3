"""
Battlehip game
"""


def print_field(field):
    """Prints the field of the game

    :param field: field to print
    :type field: list
    >>> print_field([[0, 1, 0], [1, 2, 3], [0, 0, 2]])
    0    1    0    
    1    2    3    
    0    0    2    
    >>> print_field([[0], [3], [2]])
    0    
    3    
    2    
    >>> print_field([[]])
    <BLANKLINE>
    """
    for i in  field:
        for j in range(len(i)):
            print (i[j], end= '    ')
        print()


def shoot(field):
    """Checks if it is possible to choose given coordinates in the field

    :param field: field of the game
    :type field: list
    :return: coordinates of the choosen point
    :rtype: tuple

    Unable to write doctests, input inside the function
    """
    row=int(input('Row: '))
    column=int(input('Column: '))
    try: 
        place=field[row][column]
        return (row, column)
    except: 
        print('Некоректні координати')
        shoot(field)


def init():
    """Generates an empty field

    :return: generated field
    :rtype: list

    Unable to write doctests, variable is not defined
    """
    field = [['.'] * field_sz for _ in range(field_sz)]
    return field


def init_ships(num, sizes):
    """Creates the list of ships

    :param num: number of ships
    :type num: int
    :param sizes: sizes of ship
    :type sizes: list
    :return: list of all ships
    :rtype: list
    >>> init_ships(3, [1, 2])
    [1, 1, 1, 2, 2, 2]
    >>> init_ships(1, [4, 2, 3])
    [4, 2, 3]
    >>> init_ships(2, [])
    []
    """

    ships = []

    for sz_ship in sizes:
        for _ in range(num):
            ships.append(sz_ship)

    return ships


def check_coord(row, col, battle_field):
    """Сhecks the results of the shot

    :param row: number of the raw
    :type row: int
    :param col: number of the column
    :type col: int
    :param battle_field: general field of the game
    :type battle_field: list
    :return: result of the shot
    :rtype: int

    Satus codes:
        0 - the cell killed
        1 - the cell is taken
        2 - the cell is empty (missing shot)

    >>> check_coord(0, 1, [['.', 'X'], ['.', '.']])
    1

    (expected 0, the ship is killed, 0 is unreachable)

    >>> check_coord(0, 1, [['.', '.'], ['X', 'X']])
    2
    """

    if battle_field[row][col] == '.':
        return 2
    if battle_field[row][col] == 'X':
        return 1

    return 0


def set_ship(row, col, ship_sz, battle_field):
    """Unclear function, expected to set ships on the field

    :param row: number of the row
    :type row: int
    :param col: number of the column
    :type col: int
    :param ship_sz: unused arguement
    :type ship_sz: ?
    :param battle_field: field of the battle
    :type battle_field: list

    Does not work, can't do operation int + list
    Sense of the algorithm is unclear
    """
    for i in range(row, row + battle_field + 1):
        battle_field[i][col] = 'O'


def set_ships_field(field, ships):
    """Gets coordinates from user and places ship on the game field

    :param field: field of the game
    :type field: list
    :param ships: ships needed to be placed
    :type ships: list

    Function is not working in an appropriate way
    """
    for ship in ships:
        print("Size of ship: " + str(ship) + "\nEnter your coordinate")
        coord = shoot(field)

        set_ship(coord[0], coord[1], ship, field)
        print_field(field)


def main():
    """
    Operations with user.
    """

    battle_field_1 = init(10)
    ships_1 = init_ships(3, [1, 2, 3])

    set_ships_field(battle_field_1, ships_1)

    battle_field_2 = init(10)
    ships_2 = init_ships(3, [1, 2, 3])

    set_ships_field(battle_field_2, ships_2)


# if __name__ == "__main__":
#     main()