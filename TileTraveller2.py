# 1. Which implementation was easier and why?
# 2. Which implementation is more readable and why?
# 3. Which problems in the first implementations were you able to solve with the latter
# implementation?

#  ---- GITHUB ------
# https://github.com/xioner/TileTraveller

N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

x_pos, y_pos = 1,1
acceptable_moves = ('')
direction = ''

def moving(x_pos: int, y_pos: int, direction: str)->int :
    ''' Take in current position and return a new position'''
    if direction.lower() == 'n':
        return x_pos, y_pos + 1
    elif direction.lower() == 's':
        return x_pos, y_pos - 1
    elif direction.lower() == 'e':
        return x_pos + 1, y_pos
    elif direction.lower() == 'w':
        return x_pos - 1, y_pos
    else: 
        return False

while True:
    if direction.lower() in acceptable_moves:
        if ((x_pos == 1) and (y_pos == 1)) or ((x_pos == 2) and (y_pos == 1)):
            print(f"You can travel: {N}.")
            acceptable_moves = ('n')      
        elif (x_pos == 1) and (y_pos == 2):
            print(f"You can travel: {N} or {E} or {S}.")
            acceptable_moves = ('n', 'e', 's') 
        elif (x_pos == 1) and (y_pos == 3):
            print(f"You can travel: {E} or {S}.")
            acceptable_moves = ('e', 's') 
        elif ((x_pos == 2) and (y_pos == 2)) or ((x_pos == 3) and (y_pos == 3)):
            print(f"You can travel: {S} or {W}.")
            acceptable_moves = ('s', 'w') 
        elif (x_pos == 2) and (y_pos == 3):
            print(f"You can travel: {E} or {W}.")
            acceptable_moves = ('e', 'w') 
        elif (x_pos == 3) and (y_pos == 2):
            print(f"You can travel: {N} or {S}.")
            acceptable_moves = ('n', 's') 
        elif x_pos == 3 and y_pos == 1:
            print ('Victory!')
            exit()

        x_pos, y_pos = moving(x_pos, y_pos, direction) # Function call 
    
    else: 
        print ('Not a valid direction')
        direction = str(input("Direction: ")) 

    direction = str(input("Direction: ")) 
    


# Current problem: 
# if I enter 'w' as the first input, it knows it's invalid HOWEVER it will still
# call the function and do the function's if statement, making me go to 0, 1 position
# And I will be stuck there. 