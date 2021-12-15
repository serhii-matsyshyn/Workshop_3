"""
Battlehip game
"""

"""
field =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
"""

def init():
    """
    Creating the field.
    """
    pass


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


def check_coord(row, col):
    pass






def set_ship(row, col, ship_sz):
    pass

def main():
    """
    Operations with user.
    """

    pass
