"""Template for Node implementation in Python"""
class Node:
    """Generic Python Node"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        """Set link to next node"""
        self.next_node = next_node

    def get_next_node(self):
        """Get next node object"""
        return self.next_node

    def get_value(self):
        """Return node value"""
        return self.value
