import sys

#  TODO: node object
from typing import List
from queue import PriorityQueue

class Queue:
    def __init__(self):
        self.q = list()

    def put(self, item):
        #  print("Putting " + str(i) + " into queue")
        self.q.append(item)

    def get(self):
        start = len(self.q) - 1
        end = -1
        lowest = self.q[start]
        # print(str(lowest))
        for i in range(start, end, -1):
            item = self.q[i]
            if item.h < lowest.h:
                lowest = item
                # print("New Lowest: " + str(lowest) + ", With h value: " + str(lowest.h))
        #  print(str(lowest))
        self.q.remove(lowest)
        return lowest

    def empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False


class Node:

    def __init__(self, pnum = None, ph = 0, pchildren = list(), pchange = None, pparent = None):
        self.number = pnum
        self.h = ph
        self.children = list(pchildren)
        self.previous_change = pchange
        self.parent = pparent

    def __repr__(self):
        return ''.join(str(e) for e in self.number)

    def __str__(self):
        return ''.join(str(e) for e in self.number)

    def __eq__(self, other):
        if other is None:
            return False
        if self.number == other.number:
            if self.previous_change == other.previous_change:
                return True
        return False

    def __lt__(self, other):
        if other is None:
            return True
        if self.h * (-1) < other.h * (-1):
            return True
        else:
            return False

    def get_children_numbers(self):
        c = list(self.children[0].number)
        for i in range(1, len(self.children)):
            c.append(self.children[i].number)
        return c
# -----------------------------# 
#      Build Decision Tree     # 
# -----------------------------# 

#  TODO
#  Add previous change to new nodes and h values

def get_path(node):
    path_reversed = list()
    path_reversed.append(node)
    while node.parent != None:
        path_reversed.append(node.parent)
        node = node.parent
    path = list()
    for i in range(0, len(path_reversed)):
        path.append(path_reversed.pop())
    return path

def generate_children(node, goal):
    # print("Current children for: " + str(node))
    # print(', '.join(str(e) for e in node.children))

    new_children = []
    # print("Curren new_children contents:")
    # print(new_children)
    if node.previous_change is None:
        # print("Generating root children...")
        newChild = Node()
        newChild.number = list(node.number)
        # print("Child 1 num before:")
        # print(newChild.number)
        newChild.number[0] -= 1
        # print("Child 1 num after:")
        # print(newChild.number)
        newChild.previous_change = 0
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        new_children = new_children
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[0] += 1
        newChild.previous_change = 0
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        new_children = new_children
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[1] -= 1
        newChild.previous_change = 1
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[1] += 1
        newChild.previous_change = 1
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[2] -= 1
        newChild.previous_change = 2
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[2] += 1
        newChild.previous_change = 2
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        new_children = new_children
    elif node.previous_change is 0:
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[1] -= 1
        newChild.previous_change = 1
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[1] += 1
        newChild.previous_change = 1
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[2] -= 1
        newChild.previous_change = 2
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[2] += 1
        newChild.previous_change = 2
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
    elif node.previous_change is 1:
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[0] -= 1
        newChild.previous_change = 0
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[0] += 1
        newChild.previous_change = 0
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[2] -= 1
        newChild.previous_change = 2
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[2] += 1
        newChild.previous_change = 2
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
    elif node.previous_change is 2:
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[0] -= 1
        newChild.previous_change = 0
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[0] += 1
        newChild.previous_change = 0
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[1] -= 1
        newChild.previous_change = 1
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
        newChild = Node()
        newChild.number = list(node.number)
        newChild.number[1] += 1
        newChild.previous_change = 1
        newChild.parent = node
        newChild.h = abs(goal[0] - newChild.number[0]) + abs(goal[1] - newChild.number[1]) + abs(goal[2] - newChild.number[2])
        new_children.append(newChild)
    # print("Returned children for: " + str(node))
    # print(', '.join(str(e) for e in node.children))

    #  Elimate <0 values
    # TODO: No way to do this after the fact, values <0 and <9 must be prevented from generation
    node.children = list(new_children)
    for i in range(0, len(node.children)):
        if node.children[i].number[0] < 0 or node.children[i].number[0] > 9:
            node.children.remove(node.children[i])
        elif node.children[i].number[1] < 0 or node.children[i].number[1] > 9:
            node.children.remove(node.children[i])
        elif node.children[i].number[2] < 0 or node.children[i].number[2] > 9:
            node.children.remove(node.children[i])

    #  Eliminate nodes same as parent
    return node.children


# -----------------------------# 
#           Searches           # 
# -----------------------------# 

# TODO
def a_star(root, goal, forbiddens):
    expanded = []
    fringe = Queue()
    fringe.put(root)

    while len(expanded) < 1000:
        if fringe.empty():
            print("No solution found.")
            print(','.join(str(e) for e in expanded))
            return
        n = fringe.get()
        while n in expanded or n.number in forbiddens:
            if fringe.empty():
                print("No solution found.")
                print(','.join(str(e) for e in expanded))
                return
            n = fringe.get()
        expanded.append(n)
        if n.number == goal:
            path = get_path(n)
            print(','.join(str(e) for e in path))
            print(','.join(str(e) for e in expanded))
            return
        children = generate_children(n, goal)
        # print(children)
        # print(fringe.q)
        for c in children:
            c.h += len(get_path(c))
            fringe.put(c)
        # print(fringe.q)
        # print("")
    print("No solution found.")
    print(','.join(str(e) for e in expanded))
    return



def bfs(root, goal, forbiddens):
    expanded = []
    fringe = []

    expanded.append(root)
    # print("beginning on:")
    # print(','.join(str(e) for e in expanded))
    # print("Starting search...")

    if root.number == goal:
        path = get_path(root)
        print(','.join(str(e) for e in path))
        print(','.join(str(e) for e in expanded))
        return

    for n in generate_children(root, goal):
        if (n.number in forbiddens):
            continue
        fringe.append(n)
        # print("Error checking printout:")
        # print(','.join(str(e) for e in fringe))

    for i in range(1, 1000):
        if len(fringe) == 0:
            return
        n = fringe.pop(0)
        while n in expanded or n.number in forbiddens:
            if len(fringe) == 0:
                return
            n = fringe.pop(0)
        expanded.append(n)
        if n.number == goal:
            path = get_path(n)
            # print(path)
            print(','.join(str(e) for e in path))
            print(','.join(str(e) for e in expanded))
            return
        else:
            for c in generate_children(n, goal):
                fringe.append(c)
                # print("Error checking printout:")
                # print(','.join(str(e) for e in fringe))
    # print("No solution found.")
    # print("Error checking printout:")
    # print(print(','.join(str(e) for e in expanded)))
    print("No solution found.")
    print(','.join(str(e) for e in expanded))


def dfs(root, goal, forbiddens):
    expanded = []
    fringe = []
    fringe.append(root)
    while len(expanded) < 1000:
        if len(fringe) == 0:
            print("No solution found.")
            print(','.join(str(e) for e in expanded))
            return
        n = fringe.pop(0)
        if n in expanded or n.number in forbiddens:
            continue
        expanded.append(n)

        if n.number == goal:
            path = get_path(n)
            print(','.join(str(e) for e in path))
            print(','.join(str(e) for e in expanded))
            return

        i = 0
        for c in generate_children(n, goal):
            fringe.insert(i, c)
            i += 1
    print("No solution found.")
    print(','.join(str(e) for e in expanded))

def ids(root, goal, forbiddens):

    expanded = list()
    loop_expand = list()
    fringe = list()
    max_depth = 1
    current_depth = 0
    fringe.append(root)
    while len(expanded) + len(loop_expand) < 1000:
        if len(fringe) == 0:
            expanded = expanded + loop_expand
            loop_expand = list()
            fringe = list()
            fringe.append(root)
            max_depth += 1
            continue
        n = fringe.pop(0)
        if n in loop_expand or n.number in forbiddens:
            continue

        # check it is within the current depth maximum:
        if len(get_path(n)) > max_depth:
            continue

        loop_expand.append(n)
        if n.number == goal:
            expanded = expanded + loop_expand
            path = get_path(n)
            # print(path)
            print(','.join(str(e) for e in path))
            print(','.join(str(e) for e in expanded))
            return
        else:
            i = 0
            for c in generate_children(n, goal):
                fringe.insert(i, c)
                i += 1
    expanded = expanded + loop_expand
    print("No solution found.")
    print(','.join(str(e) for e in expanded))
def greedy(root, goal, forbiddens):
    expanded = []
    fringe = Queue()
    fringe.put(root)

    while len(expanded) < 1000:
        if fringe.empty():
            print("No solution found.")
            print(','.join(str(e) for e in expanded))
            return
        n = fringe.get()
        while n in expanded or n.number in forbiddens:
            if fringe.empty():
                print("No solution found.")
                print(','.join(str(e) for e in expanded))
                return
            n = fringe.get()
        expanded.append(n)
        if n.number == goal:
            path = get_path(n)
            print(','.join(str(e) for e in path))
            print(','.join(str(e) for e in expanded))
            return
        children = generate_children(n, goal)
        # print(children)
        # print(fringe.q)
        for c in children:
            # c.h += n.h
            fringe.put(c)
        # print(fringe.q)
        # print("")
    print("No solution found.")
    print(','.join(str(e) for e in expanded))
    return

def hill_climbing(root, goal, forbiddens):
    expanded = []
    fringe = []

    expanded.append(root)

    if root.number == goal:
        path = get_path(root)
        print(','.join(str(e) for e in path))
        print(','.join(str(e) for e in expanded))
        return

    current_closest = root
    for n in generate_children(root, goal):
        if (n.h <= current_closest.h):
            current_closest = n
    if root.h == current_closest.h:
        print("No solution found.")
        print(','.join(str(e) for e in expanded))
        return
    fringe.append(current_closest)

    for i in range(1, 1000):
        if len(fringe) == 0:
            print("No solution found.")
            print(','.join(str(e) for e in expanded))
            return
        n = fringe.pop(0)
        if n.number in forbiddens or n in expanded:
            print("No solution found.")
            print(','.join(str(e) for e in expanded))
            return
        #  print (str(n) + "Was expanded")
        expanded.append(n)
        if n.number == goal:
            path = get_path(n)
            print(','.join(str(e) for e in path))
            print(','.join(str(e) for e in expanded))
            return
        current_closest = n
        for m in generate_children(n, goal):
            if (m.h <= current_closest.h):
                current_closest = m
        if current_closest.h == n.h:
            print("No solution found.")
            print(','.join(str(e) for e in expanded))
            return
        fringe.append(current_closest)
    print("No solution found.")
    print(','.join(str(e) for e in expanded))

# ------------------------------# 
#              Main             # 
# ------------------------------# 
if len(sys.argv) != 3:
    print("Invalid arguments.")
    exit(0)
search = sys.argv[1]
file = open(sys.argv[2])
start_state = file.readline().replace('\n', '')
start_state = list(start_state)
end_state = file.readline().replace('\n', '')
end_state = list(end_state)
forbidden_values_readin = file.readline().split(',')
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
decision_tree_root.h = abs(end_state[0] - decision_tree_root.number[0]) + abs(end_state[1] - decision_tree_root.number[1]) + abs(end_state[2] - decision_tree_root.number[2])

if search is 'B':
    bfs(decision_tree_root, end_state, forbidden_values)
elif search is 'D':
    dfs(decision_tree_root, end_state, forbidden_values)
elif search is 'I':
    ids(decision_tree_root, end_state, forbidden_values)
elif search is 'G':
    greedy(decision_tree_root, end_state, forbidden_values)
elif search is 'A':
    a_star(decision_tree_root, end_state, forbidden_values)
elif search is 'H':
    hill_climbing(decision_tree_root, end_state, forbidden_values)
else:
    print("Invalid search")
