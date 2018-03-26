import sys

# TODO: node object

#-----------------------------#
#     Build Decision Tree     #
#-----------------------------#

# TODO
def build_tree(start, forbiddens):

#-----------------------------#
#          Searches           #
#-----------------------------#

#TODO
def a_star():

def bfs():

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
