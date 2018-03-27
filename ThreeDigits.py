import sys

# TODO: node object

class Node(object):
    def __init__(self, number, h):
        self.number = number
        self.h = h
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

#-----------------------------#
#     Build Decision Tree     #
#-----------------------------#

# TODO
# NOTE: Tree is built until there is 1000 nodes
def build_tree(start, forbiddens):
    root = Node(start, 0)


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

    for n in root.children:
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
end_state = file.readline().reaplce('\n', '')
forbidden_values = file.readline(3).split(',')
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
