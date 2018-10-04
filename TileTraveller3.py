#Constants 
N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

x_pos, y_pos = 1,1
acceptable_moves = ('')
direction = ''
total_coins = 0 

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

def coins(total_coins):
    while True:        
        get_coins = str(input("Pull a lever (y/n): "))
        if not get_coins.lower() in 'yn':
            print("Invalid input")
            continue
        if get_coins.lower() == 'y':
            total_coins += 1
            print(f"You received 1 coins, your total is now {total_coins}.")
            break
        elif get_coins.lower() == 'n':
            break      
    return total_coins

while True: # main loop 
    if direction.lower() in acceptable_moves:
        if ((x_pos == 1) and (y_pos == 1)) or ((x_pos == 2) and (y_pos == 1)): # (1,1) / (2,1)
            print(f"You can travel: {N}.")
            acceptable_moves = ('n')   
        elif (x_pos == 1) and (y_pos == 2): # (1,2) - Coins 
            total_coins = coins(total_coins)
            print(f"You can travel: {N} or {E} or {S}.")
            acceptable_moves = ('n', 'e', 's') 
        elif (x_pos == 1) and (y_pos == 3): # (1,3) 
            print(f"You can travel: {E} or {S}.")
            acceptable_moves = ('e', 's') 
        elif ((x_pos == 2) and (y_pos == 2)): # (2,2) - Coins
            total_coins = coins(total_coins)
            print(f"You can travel: {S} or {W}.")
            acceptable_moves = ('s', 'w') 
        elif ((x_pos == 3) and (y_pos == 3)): # (3,3) 
            print(f"You can travel: {S} or {W}.")
            acceptable_moves = ('s', 'w') 
        elif (x_pos == 2) and (y_pos == 3): #  (2,3 ) - Coins 
            total_coins = coins(total_coins)
            print(f"You can travel: {E} or {W}.")
            acceptable_moves = ('e', 'w')
        elif (x_pos == 3) and (y_pos == 2): # (3,2) - Coins 
            total_coins = coins(total_coins)
            print(f"You can travel: {N} or {S}.")
            acceptable_moves = ('n', 's') 
        elif x_pos == 3 and y_pos == 1: # (3,1) - Win condition 
            print ('Victory!')
            exit()
      
    direction = str(input("Direction: ")) 
    if direction.lower() in acceptable_moves:
        x_pos, y_pos = moving(x_pos, y_pos, direction) # Function call 
    else:
        print ('Not a valid direction!')
