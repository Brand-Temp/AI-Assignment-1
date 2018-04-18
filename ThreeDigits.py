import sys

# TODO: node object

class Node:
    def __init__(self):
        self.number = None
        self.h = None
        self.children = []
        self.previous_change = None
        self.parent = None

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
def generate_children(node):
    if node.previous_change is None:
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
    return node.children


#-----------------------------#
#          Searches           #
#-----------------------------#

#TODO
def a_star():

def bfs(root, goal):
    expanded = []
    fringe = []

    expanded.append(root)

    if root.number == goal:
        path = get_path(root)
        print(path)
        print(expanded)
        return

    for n in generate_children(root):
        fringe.append(n)

    for n in fringe:
        if n in expanded:
            continue
        else:
            expanded.append(n)

            if n.number == goal:
                path = get_path(root)
                print(path)
                print(expanded)
                return
            for m in n.children:
                fringe.append(m)


def dfs():

def ids():

def greedy():

def hill_climbing():

#------------------------------#
#             Main             #
#------------------------------#
if length(sys.argv) != 3:
    print("Invalid arguments.")
    exit(0)
search = sys.argv[1]
file = open(sys.argv[2])
start_state = file.readline().replace('\n', '')
start_state = list(start_state)
end_state = file.readline().reaplce('\n', '')
end_state = list(end_state)
forbidden_values_readin = file.readline(3).split(',')
forbidden_values = []
for value in forbidden_values_readin:
    forbidden_values.append(list(value))
decision_tree_root = build_tree(start_state, forbidden_values)

if search is 'B':
    bfs(decision_tree_root, end_state)
elif search is 'D':
    dfs(decision_tree_root, end_state)
elif search is 'I':
    ids(decision_tree_root, end_state)
elif search is 'G':
    greedy(decision_tree_root, end_state)
elif search is 'A':
    a_star(decision_tree_root, end_state)
elif search is 'H':
    hill_climbing(decision_tree_root, end_state)
else:
    print("Invalid search")
