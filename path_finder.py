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

    def build_move_tree(self):
        print(self)
        start_pos = self._root.value # starting node value
        def add_children(cur_node):            
            cur_pos = cur_node.value
            new = self.new_move_positions(cur_pos)           
            
            if not new: return  # no new moves
            for new_pos in new: # add children width
                child = Node(new_pos)
                cur_node.add_child(child)             
            for child in cur_node.children:                         
                new_children = add_children(child)
                if new_children: return new_children
            return None
        add_children(self._root)








finder = KnightPathFinder((0, 0))
print (finder.new_move_positions((0, 0)))
finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder._root.children[0].value, finder._root.children[1].value)