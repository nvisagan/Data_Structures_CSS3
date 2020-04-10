import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open(r'C:\Users\navo1\Desktop\Sprint-Challenge--Data-Structures-Python\names\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(r'C:\Users\navo1\Desktop\Sprint-Challenge--Data-Structures-Python\names\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

bst = BinarySearchTree('names') 
# Replace the nested for loops below with your improvements
for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print("The runtime complexity of the previous code is O(n^2)")
print (f"runtime: {end_time - start_time} seconds")
print ("The runtime complexity is O(log n)")
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
