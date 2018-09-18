# Player starts at pos 1,1
# Depending on position, the player can either move north, south, west or east.
# Ask for direction, convert to lowercase.
# If invalid direction is entered error handle + give user a chance to redeem themselves
# east and west are on x axis
# south and north are on y axis
# If valid direction is entered by user 
# calculate new coordinates, and move on to next coordinates

# https://github.com/xioner/TileTraveller


N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'



x_pos, y_pos = 1,1
player_start = x_pos, y_pos


while True: 
    if (x_pos == 1) and (y_pos == 1) or ((x_pos == 2) and (y_pos == 1)):
        print(f"You can travel: {N}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() == 'n':
                y_pos += 1
                break
            else: 
                print ("Not a valid direction!")
                direction = str(input("Direction: "))

    if (x_pos == 1) and (y_pos == 2):
        print(f"You can travel: {N} or {E} or {S}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('n', 's', 'e'):
                if direction.lower() == 'n':
                    y_pos += 1
                    break
                elif direction.lower() == 's':
                    y_pos -= 1
                    break
                elif direction.lower() == 'e': 
                    x_pos += 1
                    break
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
              
            
    if (x_pos == 1) and (y_pos == 3):
        print(f"You can travel: {E} or {S}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('s', 'e'):
                if direction.lower() == 's':
                    y_pos -= 1
                    break
                elif direction.lower() == 'e': 
                    x_pos += 1
                    break
            else: 
                print("Not a valid direction!")
                direction = str(input("Direction: "))

    if ((x_pos == 2) and (y_pos == 2)) or ((x_pos == 3) and (y_pos == 3)):
        print(f"You can travel: {S} or {W}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('w', 's'):
                if direction.lower() == 'w':
                    x_pos -= 1
                    break
                elif direction.lower() == 's': 
                    y_pos -= 1
                    break
            else: 
                print("Not a valid direction!")
                direction = str(input("Direction: "))

    if (x_pos == 2) and (y_pos == 3):
        print(f"You can travel: {E} or {W}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('e', 'w'):
                if direction.lower() == 'e':
                    x_pos += 1
                    break
                elif direction.lower() == 'w':
                    x_pos -= 1
                    break
            else: 
                print("Not a valid direction!")
                direction = str(input("Direction: "))           

    if (x_pos == 3) and (y_pos == 2):
        print(f"You can travel: {N} or {S}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('n','s'):
                if direction.lower() == 'n':
                    y_pos += 1
                    break
                elif direction.lower() == 's': 
                    y_pos -= 1
                    break
            else: 
                print("Not a valid direction!")
                direction = str(input("Direction: "))

    if x_pos == 3 and y_pos == 1:
        print ('Victory!')
        exit()