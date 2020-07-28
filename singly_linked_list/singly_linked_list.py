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

    def insert_after(self, value):
        current_next = get_next()
        self.next = ListNode(value, next_node=current_next)
        if current_next is not None:
            current_next.prev = self.next

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev

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
        if self.head is None:
            return None
        else:
            current_node = self.head
            biggest = self.head.get_value()
            while current_node is not None:
                if current_node.get_value() > biggest:
                    biggest = current_node.get_value()
                current_node = current_node.get_next()
            return biggest

    def reverse(self):
        current_node = self.head 
        prev_node = None
        while(current_node is not None): 
            next_node = current_node.next
            current_node.next = prev_node 
            prev_node = current_node 
            current_node = next_node
        self.head = prev_node