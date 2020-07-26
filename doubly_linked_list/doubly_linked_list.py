"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return (f"ListNode("
                f"\n\tvalue={self.value}"
                f"\n\tprev={self.prev}"
                f"\n\tnext={self.next}\n)")

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, prev=current_prev, next=self)
        if current_prev is not None:
            current_prev.next = self.prev
            

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, prev=self, next=current_next)
        if current_next is not None:
            current_next.prev = self.next

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return (f"DoublyLinkedList"
                f"<\n\thead={self.head!r}"
                f"\n\ttail={self.tail!r}"
                f"\n\tlength={self.length}\n>")
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        deleted_head = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.delete()
            self.head = deleted_head.next
        self.length -= 1
        return deleted_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        deleted_tail = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
            self.tail = deleted_tail.prev
        self.length -= 1
        return deleted_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.tail:
            self.remove_from_tail()
        elif node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            self.remove_from_tail()
        elif node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is self.tail:
            self.remove_from_tail()
        elif node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is self.tail:
            return self.head.value
        biggest = self.head.value
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value > biggest:
                biggest = current_node.value
        return biggest
        