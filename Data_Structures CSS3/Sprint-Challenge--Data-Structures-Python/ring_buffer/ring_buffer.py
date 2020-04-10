from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    #FIFO
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if the storage is not full
        if self.storage.length < self.capacity:
            #add to  tail
            self.storage.add_to_tail(item)
            #then update the current
            self.current = self.storage.head
        #If storage is full
        elif self.storage.length == self.capacity:
            #remove the oldest item, the head
            drop = self.storage.head
            self.storage.remove_from_head()
            #add new item
            self.storage.add_to_tail(item)
            #if at head, set current position to tail 
            if drop == self.current:
                self.current = self.storage.tail 

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        start = self.current
        list_buffer_contents.append(start.value)
        #go through each node and append vaue to buffer
        if start.next:
            nxt = start.next
        else:
            nxt = self.storage.head

        while nxt != start:
            list_buffer_contents.append(nxt.value)
            if nxt.next:
                nxt=nxt.next
            else:
                nxt = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
