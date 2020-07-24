class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self. tail = None
        self.length = 0

    def get_length(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def contains(self, value):
        # 1. use a loop to iterate through the linked list
        current_node = self.head
        while current_node is not None:
        # 2. check if the value of the current nod is the value we're searching for
            if value == current_node.get_value():
                return True
            current_node = current_node.get_next()
        return False
        # 3. Return true if found, falst if we reach the end of the list
        
            

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head.get_next() is None:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
            

    def get_max(self):
        if self.length == 0:
            return None
        else:
            global current_node
            global next_node
            global biggest
            current_node = self.head
            next_node = self.head.get_next()
            biggest = current_node.value
            while current_node.get_next() != None:
                if next_node.get_value() > current_node.get_value():
                    biggest = next_node.get_value()
                    current_node = next_node
                    next_node = current_node.get_next()
                else:
                    current_node = next_node
                    next_node = current_node.get_next()
            return biggest