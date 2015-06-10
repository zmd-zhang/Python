"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    line_nozero=[]
    line_zero=[]
    result=[]
    for line_index in range(0,len(line)):
        if line[line_index]!=0:
            line_nozero.append(line[line_index])
        else:
            line_zero.append(0)

    nozero_index=0

    while nozero_index<len(line_nozero):
        if nozero_index==(len(line_nozero)-1):
            result.append(line_nozero[nozero_index])
            nozero_index=nozero_index+1
        elif line_nozero[nozero_index]==line_nozero[nozero_index+1]:
            result.append(line_nozero[nozero_index]+line_nozero[nozero_index+1])
            line_zero.append(0)
            nozero_index=nozero_index+2
        else:
            result.append(line_nozero[nozero_index])
            nozero_index=nozero_index+1
    return result+line_zero

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height=grid_height
        self._width=grid_width
        self._cells=[]
        self.reset()
        self._initial_tiles={UP:[[0,e_index] for e_index in range(self._width)],
                            DOWN:[[self._height-1,e_index] for e_index in range(self._width)],
                            LEFT:[[e_index,0] for e_index in range(self._height)],
                            RIGHT:[[e_index,self._width-1] for e_index in range(self._height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells=[[0 for dummy_col in range(self.get_grid_width())]
                        for dummy_row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._cells)



    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tile_changed=False
        if direction in (UP,DOWN):
            length=self.get_grid_height()
        elif direction in (LEFT, RIGHT):
            length=self.get_grid_width()
            
        for cell_index in self._initial_tiles[direction]:
            temp_list=[]

            for step in range(length):
                row=cell_index[0]+step*OFFSETS[direction][0]
                col=cell_index[1]+step*OFFSETS[direction][1]
                temp_list.append(self._cells[row][col])
                
            temp_list=merge(temp_list)
            
            tl_index=0
            
            for step in range(length):
                row=cell_index[0]+step*OFFSETS[direction][0]
                col=cell_index[1]+step*OFFSETS[direction][1]
                
                if self._cells[row][col]!=temp_list[tl_index]:
                    tile_changed=True
                    
                self._cells[row][col]=temp_list[tl_index]
                tl_index=tl_index+1
        if tile_changed:
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zero_cells=[]
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row][col]==0:
                    zero_cells.append([row,col])
        random_cell=random.choice(zero_cells)
      
        if random.random()>0.1:
            new_value=2
        else:
            new_value=4
            
        self.set_tile(random_cell[0],random_cell[1],new_value)
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col]=value
                

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
#test_grid = TwentyFortyEight(2, 3)
#print test_grid
