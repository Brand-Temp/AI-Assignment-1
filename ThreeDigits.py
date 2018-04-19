import sys

# TODO: node object
from typing import List


class Node:
    def __init__(self):
        self.number = None
        self.h = None
        self.children = []
        self.previous_change = None
        self.parent = None

    def __str__(self):
        return ''.join(str(e) for e in self.number)

    def __repr__(self):
        return ''.join(str(e) for e in self.number)

    def __eq__(self, other):
        if self.number == other.number:
            if self.previous_change == other.previous_change:
                return True
        return False
#-----------------------------#
#     Build Decision Tree     #
#-----------------------------#

# TODO
# Add previous change to new nodes and h values

def get_path(node):
    return "Make Path"

def generate_children(node):
    if node.previous_change is None:
        new_children = []
        print("Generating root children...")
        newChild = Node()
        newChild.number = node.number
        print("Child 1 num before:")
        print(newChild.number)
        newChild.number[0] -= 1
        print("Child 1 num after:")
        print(newChild.number)
        newChild.previous_change = 0
        newChild.parent = node
        new_children.append(newChild)
        for c in new_children:
            print(c.number)
        node.children = new_children
        newChild = Node()
        newChild.number = node.number
        newChild.number[0] += 1
        newChild.previous_change = 0
        newChild.parent = node
        new_children.append(newChild)
        for c in new_children:
            print(c.number)
        node.children = new_children
        newChild = Node()
        newChild.number = node.number
        newChild.number[1] -= 1
        newChild.previous_change = 1
        newChild.parent = node
        new_children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[1] += 1
        newChild.previous_change = 1
        newChild.parent = node
        new_children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[2] -= 1
        newChild.previous_change = 2
        newChild.parent = node
        new_children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[2] += 1
        newChild.previous_change = 2
        newChild.parent = node
        new_children.append(newChild)
        print("New_Children:")
        for c in new_children:
            print(c.number)
        node.children = new_children
    elif node.previous_change is 0:
        newChild = Node()
        newChild.number = node.number
        newChild.number[1] -= 1
        newChild.previous_change = 1
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[1] += 1
        newChild.previous_change = 1
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[2] -= 1
        newChild.previous_change = 2
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[2] += 1
        newChild.previous_change = 2
        newChild.parent = node
        node.children.append(newChild)
    elif node.previous_change is 1:
        newChild = Node()
        newChild.number = node.number
        newChild.number[0] -= 1
        newChild.previous_change = 0
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[0] += 1
        newChild.previous_change = 0
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[2] -= 1
        newChild.previous_change = 2
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[2] += 1
        newChild.previous_change = 2
        newChild.parent = node
        node.children.append(newChild)
    elif node.previous_change is 2:
        newChild = Node()
        newChild.number = node.number
        newChild.number[0] -= 1
        newChild.previous_change = 0
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[0] += 1
        newChild.previous_change = 0
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[1] -= 1
        newChild.previous_change = 1
        newChild.parent = node
        node.children.append(newChild)
        newChild = Node()
        newChild.number = node.number
        newChild.number[1] += 1
        newChild.previous_change = 1
        newChild.parent = node
        node.children.append(newChild)
    print("Returned children:")
    print(','.join(str(e) for e in node.children))
    return node.children


#-----------------------------#
#          Searches           #
#-----------------------------#

#TODO
def a_star():
    return

def bfs(root, goal, forbiddens):
    expanded = []
    fringe = []

    expanded.append(root)
    print("beginning on:")
    print(print(','.join(str(e) for e in expanded)))
    print("Starting search...")

    if root.number == goal:
        path = get_path(root)
        print(path)
        print(','.join(str(e) for e in expanded))
        return

    for n in generate_children(root):
        if (n.number in forbiddens):
            continue
        fringe.append(n)

    for i in range(0, 50):
        n = fringe.pop(0)
        if n.number == goal:
            path = get_path(n)
            print(path)
            print(','.join(str(e) for e in expanded))
            return
        else:
            for c in generate_children(n):
                if c.number in forbiddens:
                    continue
                fringe.append(c)
    print("No solution found.")
    print("Error checking printout:")
    print(print(','.join(str(e) for e in expanded)))


def dfs():
    return

def ids():
    return

def greedy():
    return

def hill_climbing():
    return

#------------------------------#
#             Main             #
#------------------------------#
if len(sys.argv) != 3:
    print("Invalid arguments.")
    exit(0)
search = sys.argv[1]
file = open(sys.argv[2])
start_state = file.readline().replace('\n', '')
start_state = list(start_state)
end_state = file.readline().replace('\n', '')
end_state = list(end_state)
forbidden_values_readin = file.readline(3).split(',')
forbidden_values = []
for value in forbidden_values_readin:
    forbidden_values.append(list(value))

for i in range(0, 3):
    start_state[i] = int(start_state[i])
    end_state[i] = int(end_state[i])
for i in range(0, len(forbidden_values)):
    for j in range(0, len(forbidden_values[i])):
        forbidden_values[i][j] = int(forbidden_values[i][j])

decision_tree_root = Node()
decision_tree_root.number = start_state


if search is 'B':
    bfs(decision_tree_root, end_state, forbidden_values)
#elif search is 'D':
#    dfs(decision_tree_root, end_state)
#elif search is 'I':
#    ids(decision_tree_root, end_state)
#elif search is 'G':
#    greedy(decision_tree_root, end_state)
#elif search is 'A':
#    a_star(decision_tree_root, end_state)
#elif search is 'H':
#    hill_climbing(decision_tree_root, end_state)
#else:
    #print("Invalid search")
