import bottomCrossCases
import moves
rubiks_cube={'F1': 'O', 'F2': 'R', 'F3': 'O', 'F4': 'Y', 'F5': 'R', 'F6': 'O', 'F7': 'B', 'F8': 'Y', 'F9': 'Y', 'R1': 'G', 'R2': 'O', 'R3': 'B', 'R4': 'B', 'R5': 'G', 'R6': 'B', 'R7': 'G', 'R8': 'G', 'R9': 'W', 'B1': 'O', 'B2': 'Y', 'B3': 'W', 'B4': 'W', 'B5': 'O', 'B6': 'O', 'B7': 'R', 'B8': 'O', 'B9': 'O', 'L1': 'R', 'L2': 'R', 'L3': 'G', 'L4': 'W', 'L5': 'B', 'L6': 'G', 'L7': 'Y', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'W', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'Y', 'U8': 'B', 'U9': 'W', 'D1': 'Y', 'D2': 'R', 'D3': 'R', 'D4': 'G', 'D5': 'W', 'D6': 'W', 'D7': 'B', 'D8': 'Y', 'D9': 'G'}

# cases and moves for each situation
def bring_piece_to_F8(rubiks_cube,side_pieces,moving_piece):
    if(moving_piece==side_pieces[0]):
        return bottomCrossCases.piece_on_front_top(rubiks_cube)
    elif(moving_piece==side_pieces[1]):
        return bottomCrossCases.piece_on_front_left(rubiks_cube)
    elif(moving_piece==side_pieces[2]):
        return bottomCrossCases.piece_on_front_right(rubiks_cube)
    elif(moving_piece==side_pieces[3]):
        return bottomCrossCases.piece_on_front_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[4]):
        return bottomCrossCases.piece_on_back_top(rubiks_cube)
    elif(moving_piece==side_pieces[5]):
        return bottomCrossCases.piece_on_left_top(rubiks_cube)
    elif(moving_piece==side_pieces[6]):
        return bottomCrossCases.piece_on_right_top(rubiks_cube)
    elif(moving_piece==side_pieces[7]):
        return bottomCrossCases.piece_on_right_right(rubiks_cube)
    elif(moving_piece==side_pieces[8]):
        return bottomCrossCases.piece_on_left_left(rubiks_cube)
    elif(moving_piece==side_pieces[9]):
        return bottomCrossCases.piece_on_back_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[10]):
        return bottomCrossCases.piece_on_right_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[11]):
        return bottomCrossCases.piece_on_left_bottom(rubiks_cube)
    
# to dectect the white piece
def dectect_required_side_pieces(rubiks_cube,side_pieces):
    white_side_piece_positions=[]
    for pair in side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['D5']:  # Check if the position has a white piece
                white_side_piece_positions.append(pair)    

    return white_side_piece_positions


# function to get the white and front center colored piece 
def frontCenter_piece_position(rubiks_cube,white_side_pieces):
    fc_colored_piece_position=[]
    for pair in white_side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                fc_colored_piece_position=pair
    return fc_colored_piece_position


def bottomCross(rubiks_cube):
    side_pieces=[['F2','U8'],['F4','L6'],['F6','R4'],['F8','D2'],['U2','B2'],['U4','L2'],['U6','R2'],['B4','R6'],['B6','L4'],['B8','D8'],['R8','D6'],['L8','D4']]
    sequence=[]
    for i in range(4):
        moves.print_2d_cube(rubiks_cube)
        required_side_pieces=dectect_required_side_pieces(rubiks_cube,side_pieces)
        print(required_side_pieces)

        required_piece=frontCenter_piece_position(rubiks_cube,required_side_pieces)
        print(required_piece)
        
        face_moves=bring_piece_to_F8(rubiks_cube,side_pieces,required_piece)
        print(face_moves)
        for move in face_moves:
            rubiks_cube = moves.execute_move(rubiks_cube, move)
            moves.print_2d_cube(rubiks_cube) 
        
        rubiks_cube=moves.rotateLeft(rubiks_cube)
        moves.print_2d_cube(rubiks_cube)
        sequence.extend(face_moves)
        sequence.append('rl')
    return sequence

print(bottomCross(rubiks_cube))