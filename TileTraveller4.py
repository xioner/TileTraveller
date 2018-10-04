#Constants 
N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'



def moving(col:int, row:int, direction:str)->int :
    ''' Take in current position and return a new position'''

    if direction.lower() == 'n':
        row += 1
    elif direction.lower() == 's':
        row -= 1
    elif direction.lower() == 'e':
        col += 1 
    elif direction.lower() == 'w':
        col -= 1
    return col, row

def coins(total_coins:int) -> int:
    ''' Cunting coins '''
    while True:        
        get_coins = str(input("Pull a lever (y/n): "))
        get_coins = get_coins.lower()
        if not get_coins in 'yn':
            print("Invalid input")
            continue
        if get_coins == 'y':
            total_coins += 1
            print(f"You received 1 coins, your total is now {total_coins}.")
            break
        elif get_coins == 'n':
            break      
    return total_coins

def play_again():
    ''' Checks whether user would like to play again'''
    while True:
        play_again = str(input("Play again (y/n): "))
        if not play_again in 'yn':
            print("Invalid input")
            continue
        if play_again == 'y':
            return True
        elif play_again == 'n':
            exit()

def play(victory, direction, acceptable_moves, col, row, total_coins):
    ''' Main game '''
    while not victory: # main loop 
        if direction in acceptable_moves:
            if ((col == 1) and (row == 1)) or ((col == 2) and (row == 1)): # (1,1) / (2,1)
                print(f"You can travel: {N}.")
                acceptable_moves = ('n')   
            elif (col == 1) and (row == 2): # (1,2) - Coins 
                total_coins = coins(total_coins)
                print(f"You can travel: {N} or {E} or {S}.")
                acceptable_moves = ('n', 'e', 's') 
            elif (col == 1) and (row == 3): # (1,3) 
                print(f"You can travel: {E} or {S}.")
                acceptable_moves = ('e', 's') 
            elif (col == 2) and (row == 2): # (2,2) - Coins
                total_coins = coins(total_coins)
                print(f"You can travel: {S} or {W}.")
                acceptable_moves = ('s', 'w') 
            elif (col == 3) and (row == 3): # (3,3) 
                print(f"You can travel: {S} or {W}.")
                acceptable_moves = ('s', 'w') 
            elif (col == 2) and (row == 3): #  (2,3 ) - Coins 
                total_coins = coins(total_coins)
                print(f"You can travel: {E} or {W}.")
                acceptable_moves = ('e', 'w')
            elif (col == 3) and (row == 2): # (3,2) - Coins 
                total_coins = coins(total_coins)
                print(f"You can travel: {N} or {S}.")
                acceptable_moves = ('n', 's') 
            elif col == 3 and row == 1: # (3,1) - Win condition 
                print ('Victory!')
                if play_again():
                    victory = False
                    col, row = 1, 1
                    total_coins = 0
                    print(f"You can travel: {N}.")
        
        direction = str(input("Direction: ")) 
        direction = direction.lower()
        if direction in acceptable_moves:
            col, row = moving(col, row, direction) # Function call 
        else:
            print ('Not a valid direction!')

col, row = 1,1
acceptable_moves = ('')
direction = ''
total_coins = 0
victory = False


play(victory, direction, acceptable_moves, col, row, total_coins)
