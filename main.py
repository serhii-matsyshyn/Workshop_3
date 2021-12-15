"""
Battlehip game
"""

def print_field(field):
    for i in  field:
        for j in range(len(i)):
            print (i[j], end= '    ')
        print()


def shoot(field):
    row=int(input('Row: '))
    column=int(input('Column: '))
    try: 
        place=field[row][column]
        return (row, column)
    except: 
        print('Некоректні координати')
        shoot(field)


def init():
    field = [['.'] * field_sz for _ in range(field_sz)]
    return field


def init_ships(num, sizes):
    """
    Create the list of ships.
    """

    ships = []

    for sz_ship in sizes:
        for _ in range(num):
            ships.append(sz_ship)

    return ships


def check_coord(row, col, battle_field):
    """
    Satus codes:
        0 - the cell killed
        1 - the cell is taken
        2 - the cell is empty (missing shot)
    """

    if battle_field[row][col] == '.':
        return 2
    if battle_field[row][col] == 'X':
        return 1

    return 0


def set_ship(row, col, ship_sz, battle_field):
    for i in range(row, row + battle_field + 1):
        battle_field[i][col] = 'O'


def set_ships_field(field, ships):
    for ship in ships:
        print("Size of ship: " + str(ship) + "\nEnter your coordinate")
        coord = shoot()

        set_ship(coord[0], coord[1], ship, field)
        print_field(field)


def main():
    """
    Operations with user.
    """

    battle_field_1 = init(10)
    ships_1 = init_ships(3, [1, 2, 3])

    set_ships_field(battle_field_1, ships_1)

    battle_field_2 = inti(10)
    ships_2 = init_ships(3, [1, 2, 3])

    set_ships_field(battle_field_2, ships_2)


if __name__ == "__main__":
    main()