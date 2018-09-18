## Tile Traveller

<p>This assignment contains two parts. You need to implement one program in each part and you
have to use git during the development. Create one directory, named TileTraveller, on your
local computer that will contain the two programs. In addition, you need to push your solution to
github.</p>

The assignment is to develop a computer game in which the player is located in a certain tile in
a grid. At each iteration, the program displays the directions for which there are adjacent tiles
that the player can travel to.

The program only displays text, so you don’t actually draw the tile grid, but the program should
behave as if the player is in a 3x3 grid with open and closed walls as seen in the following image: 

![chrome_2018-09-18_16-55-16](https://user-images.githubusercontent.com/9305163/45704029-742d0a80-bb65-11e8-9776-f808dc0eda9b.png)


The player starts in tile (1,1). At the beginning, and after each move selected by the player, the
program should print the player’s travel options. If there is an open wall in a direction, write that
direction as a possible travel direction.

At each iteration, the player enters the first letter of the direction he/she wishes to travel, after
which the player should “be” in another tile and the options for the new tile are then printed out.

The player enters:<br/>
• n/N for north (up)<br/>
• e/E for east (right)<br/>
• s/S for south (down)<br/>
• w/W for west (left)<br/>

If the player enters an invalid direction, the program prints “Not a valid direction!” and allows the
player to enter the direction again.

For example, in tile (1,1) it’s only possible to move north. In tile (1,2), the possible moves are
north, east and south, and in tile (3,3) the valid moves are south and west.

Tile (3,1) is the victory location. When the player enters this tile the program should notify
him/her of their victory and quit running.


### First implementation

This implementation is without the use of functions.


### Second implementation

Code is refactored with the use of functions. 
