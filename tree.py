class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []
    
    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children
    
    def add_child(self, node):
        if node not in self._children:
            self._parent = node  #?
        self._children.append(node)

    def remove_child(self, node):
        self._children.pop(node)
        self._parent = None

    @property
    def parent(self):
        return self._parent
    


    
