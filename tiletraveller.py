# The player enters:
# • n/N for north (up)
# • e/E for east (right)
# • s/S for south (down)
# • w/W for west (left)

# If the player enters an invalid direction, the program prints “Not a valid direction!” 
# and allows the player to enter the direction again.

# (1,1) in ('north')
# (1,2) in ('north', 'south', 'east')
# (1,3) in ('north', 'east')
# (2,1) in ('east')
# (2,2) in ('west', 'south')
# (2,3) in ('north')
# (3,3) in ('west', 'south')
# (3,2) in ('north', 'south')

N = '(N)orth'
S = '(S)outh'
E = '(E)east'
W = '(W)est'



x_pos, y_pos = 1,1
player_start = x_pos, y_pos
# start = print (f"You can travel: (N)orth")



while True: 
    if x_pos == 1 and y_pos == 1:
        print("You can travel (N)orth")
    direction = str(input("Direction: "))
    if direction.lower() == 'n':
        y_pos += 1
    else: 
        print ("Not a valid direction!")

    if x_pos == 1 and y_pos == 2:
        print(f"You can travel: {N}, {S}, {E}")
        direction = str(input("Direction: "))
        if direction.lower() == 'n' or 's' or 'e':
            if direction.lower() == 'n':
                y_pos += 1
                print ('Moved north')
            if direction.lower() == 's':
                y_pos -= 1
                print('Moved south')
            if direction.lower() == 'e': 
                x_pos += 1
                print ('Moved east')
        else: 
            print("Not a valid direction!")

    if x_pos == 1 and y_pos == 3:
        print(f"You can travel: {S}, {E}")
        direction = str(input("Direction: "))
        if direction.lower() == 's' or 'e':
            if direction.lower() == 's':
                y_pos -= 1
                print('Moved south')
            if direction.lower() == 'e': 
                x_pos += 1
                print ('Moved east')
        else: 
            print("Not a valid direction!")

    if x_pos == 2 and y_pos == 1:
        print(f"You can travel: {E}")
        direction = str(input("Direction: "))
        if direction.lower() == 'e': 
                x_pos += 1
                print ('Moved east')
        else: 
            print("Not a valid direction!")

    if x_pos == 2 and y_pos == 2:
        print(f"You can travel: {W}, {S}")
        direction = str(input("Direction: "))
        if direction.lower() == 's' or 'w':
            if direction.lower() == 's':
                y_pos -= 1
                print('Moved south')
            if direction.lower() == 'w': 
                x_pos -= 1
                print ('Moved west')
        else: 
            print("Not a valid direction!")

    if x_pos == 2 and y_pos == 3:
        print(f"You can travel: {E}")
        direction = str(input("Direction: "))
        if direction.lower() == 'e':
            if direction.lower() == 'e':
                x_pos += 1
                print('Moved east')
        else: 
            print("Not a valid direction!")           

    if x_pos == 3 and y_pos == 3:
        print(f"You can travel: {W}, {S}")
        direction = str(input("Direction: "))
        if direction.lower() == 's' or 'w':
            if direction.lower() == 's':
                y_pos -= 1
                print('Moved south')
            if direction.lower() == 'w': 
                x_pos -= 1
                print ('Moved west')
        else: 
            print("Not a valid direction!")

    if x_pos == 3 and y_pos == 2:
        print(f"You can travel: {N}, {S}")
        direction = str(input("Direction: "))
        if direction.lower() == 'n' or 's':
            if direction.lower() == 'n':
                y_pos += 1
                print('Moved north')
            if direction.lower() == 's': 
                y_pos -= 1
                print ('Moved south')
        else: 
            print("Not a valid direction!")

    if x_pos == 3 and y_pos == 1:
        print (5*"\nVictory!!")
        exit()
    
