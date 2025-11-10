# LISTS
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print("List:", fruits)
fruits.remove("banana")
print("After removal:", fruits)
print("First item:", fruits[0])

# STACKS (LIFO)
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print("\nStack after pushes:", stack)
stack.pop()
print("Stack after pop:", stack)

# QUEUES (FIFO)
from collections import deque

queue = deque(["A", "B", "C"])
print("\nInitial queue:", queue)
queue.append("D")
print("After enqueue:", queue)
queue.popleft()
print("After dequeue:", queue)

# SETS
numbers = {1, 2, 3, 3, 4}
print("\nSet:", numbers)
numbers.add(5)
print("After adding 5:", numbers)
numbers.remove(3)
print("After removing 3:", numbers)

# DICTIONARIES
student = {"name": "Chrishelle", "age": 23, "course": "Software Engineering"}
print("\nStudent name:", student["name"])
student["age"] = 24
print("Updated dictionary:", student)

# LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

print("\nLinked List Example:")
ll = LinkedList()
ll.append("Node 1")
ll.append("Node 2")
ll.append("Node 3")
ll.display()

# TREE
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")

print("\nTree Example:")
print("Root:", root.value)
print("Left child:", root.left.value)
print("Right child:", root.right.value)

# GRAPH
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("\nGraph Example:")
for node, edges in graph.items():
    print(f"{node} -> {edges}")
