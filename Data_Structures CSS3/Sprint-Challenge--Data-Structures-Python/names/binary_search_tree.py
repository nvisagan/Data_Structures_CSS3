class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #First Compare with root 
        if value < self.value:
            #if value is less then be a left child
            if  self.left is None:
                self.left = BinarySearchTree(value)
                #recurse
            else:
                self.left.insert(value)
            
        else: #when value is greater than root node
            #greater or equal to go right
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
            #if the target is same as the root or for recurse
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)