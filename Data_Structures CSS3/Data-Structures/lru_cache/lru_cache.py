from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]

        else:
            return None
            

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # check and see if the key is in dict
        if key in self.storage:
            #if it is 
            node = self.storage[key]
            #overwrite the value
            node.value = (key, value)
            # move it to the end
            self.order.move_to_end(node)
            #nothing else to do, so exit function
            return

        #check and see if cache is full
        if self.size == self.limit:
            #remove oldest entry from dictionary
            del self.storage[self.order.head.value[0]]
            # AND LL
            self.order.remove_from_head()
            self.size -=1

        # ADD TO THE LINKED LIST (KEY AND THE VALUE)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary 
        self.storage[key] = self.order.tail
        #increment size
        self.size += 1
        
        