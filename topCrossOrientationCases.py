import moves
rubiks_cube={'F1': 'Y', 'F2': 'R', 'F3': 'O', 'F4': 'G', 'F5': 'G', 'F6': 'G', 'F7': 'G', 'F8': 'G', 'F9': 'G', 'R1': 'Y', 'R2': 'B', 'R3': 'Y', 'R4': 'O', 'R5': 'O', 'R6': 'O', 'R7': 'O', 'R8': 'O', 'R9': 'O', 'B1': 'R', 'B2': 'O', 'B3': 'Y', 'B4': 'B', 'B5': 'B', 'B6': 'B', 'B7': 'B', 'B8': 'B', 'B9': 'B', 'L1': 'O', 'L2': 'G', 'L3': 'R', 'L4': 'R', 'L5': 'R', 'L6': 'R', 'L7': 'R', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'Y', 'U3': 'G', 'U4': 'Y', 'U5': 'Y', 'U6': 'Y', 'U7': 'B', 'U8': 'Y', 'U9': 'G', 'D1': 'W', 'D2': 'W', 'D3': 'W', 'D4': 'W', 'D5': 'W', 'D6': 'W', 'D7': 'W', 'D8': 'W', 'D9': 'W'}


def correct_orientation(rubiks_cube):
    correct=False
    sequence=[]
    adjacent_colors={}
    adjacent_colors[rubiks_cube['F5']]=rubiks_cube['R5']
    adjacent_colors[rubiks_cube['R5']]=rubiks_cube['B5']
    adjacent_colors[rubiks_cube['B5']]=rubiks_cube['L5']
    adjacent_colors[rubiks_cube['L5']]=rubiks_cube['F5']
    front_color=rubiks_cube['F2']
    back_color=rubiks_cube['B2']
    left_color=rubiks_cube['L2']
    right_color=rubiks_cube['R2']
    print(adjacent_colors)
    moves.print_2d_cube(rubiks_cube)
    if adjacent_colors[front_color]==right_color and adjacent_colors[right_color]==back_color and adjacent_colors[back_color]==left_color and adjacent_colors[left_color]==front_color:
        correct=True

    if correct:
        for x in range(4):
            if rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5'] and rubiks_cube['F2']==rubiks_cube['F5']:
                correct=True
                if sequence==['u','u','u']:
                    sequence=["u'"]
                return correct, sequence
            rubiks_cube=moves.execute_move(rubiks_cube,'u')
            sequence.append('u')
    return correct,sequence

def opossite_colors(rubiks_cube):
    sequence=[]
    opposite_colors={}
    opposite_colors[rubiks_cube['F5']]=rubiks_cube['B5']
    opposite_colors[rubiks_cube['B5']]=rubiks_cube['F5']
    opposite_colors[rubiks_cube['U5']]=rubiks_cube['D5']
    opposite_colors[rubiks_cube['D5']]=rubiks_cube['U5']
    opposite_colors[rubiks_cube['R5']]=rubiks_cube['L5']
    opposite_colors[rubiks_cube['L5']]=rubiks_cube['R5']
    front_color=rubiks_cube['F2']
    back_color=rubiks_cube['B2']
    left_color=rubiks_cube['L2']
    right_color=rubiks_cube['R2']
    print(opposite_colors)
    moves.print_2d_cube(rubiks_cube)
    opposite=False
    if opposite_colors[front_color]==back_color or opposite_colors[right_color]==left_color:
        opposite=True
    if opposite:
        if opposite_colors[front_color]==back_color:
            sequence.extends(['b','u',"b'",'u','b',"u'","u'","b'"])
            sequence.extends(adjacent_colors(rubiks_cube))
        elif opposite_colors[right_color]==left_color:
            sequence.extends(['r','u',"r'",'u','r',"u'","u'","r'"])
            sequence.extends(adjacent_colors(rubiks_cube))
    return opposite,sequence

def adjacent_colors(rubiks_cube):
    sequence=[]
    adjacent_colors={}
    adjacent_colors[rubiks_cube['F5']]=rubiks_cube['R5']
    adjacent_colors[rubiks_cube['R5']]=rubiks_cube['B5']
    adjacent_colors[rubiks_cube['B5']]=rubiks_cube['L5']
    adjacent_colors[rubiks_cube['L5']]=rubiks_cube['F5']
    front_color=rubiks_cube['F2']
    back_color=rubiks_cube['B2']
    left_color=rubiks_cube['L2']
    right_color=rubiks_cube['R2']
    print(adjacent_colors)
    moves.print_2d_cube(rubiks_cube)
    adjacent=False
    if adjacent_colors[front_color]==right_color or adjacent_colors[right_color]==back_color or adjacent_colors[back_color]==left_color or adjacent_colors[left_color]==front_color:
        adjacent=True
    if adjacent:
        if adjacent_colors[front_color]==right_color:
            sequence.extends(['f','u',"f'",'u','f',"u'","u'","f'"])
        elif adjacent_colors[right_color]==back_color:
            sequence.extend(['r','u',"r'",'u','r',"u'","u'","r'"])
        elif adjacent_colors[back_color]==left_color:
            sequence.extend(['b','u',"b'",'u','b',"u'","u'","b'"])
        elif adjacent_colors[left_color]==front_color:
            sequence.extend(['l','u',"l'",'u','l',"u'","u'","l'"])
    return adjacent,sequence


def dectect_cube_orientation(rubiks_cube):
    # opposite or not 
    if opossite_colors(rubiks_cube):
        print('opposite')
    else:
        print('not opposite')

print(correct_orientation(rubiks_cube))