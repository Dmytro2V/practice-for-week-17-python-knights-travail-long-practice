from tree import Node

class KnightPathFinder:
    def __init__(self, xy):
        self.xy = xy
        self._root = Node(xy)
        self._considered_positions = set(xy)
    
    def get_valid_moves(self, pos): # returns valid new positions, not moves
        valid = set()
        move_opts = [(1, 2), (1,-2), (-1, 2), (-1, -2),
                     (2, 1), (2, -1), (-2, 1), (-2, -1)]
        
        for move in move_opts:
            (x0, y0) = pos
            x1 = x0 + move[0]
            y1 = y0 + move[1]
            if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                valid.add((x1, y1))
        return valid

    def new_move_positions(self, pos):        
        valid = self.get_valid_moves(pos) 
        new =  valid - self._considered_positions
        self._considered_positions.update(new) # adding only new valid pos
        return new


finder = KnightPathFinder((0, 0))
print (finder.new_move_positions((0, 0)))