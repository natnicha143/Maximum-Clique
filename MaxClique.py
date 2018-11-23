#-----------------#
# Name: Natnicha  #
#-----------------#
import time
import random as rand
import numpy as np


def initialise_graph():
    with open("graph_files/" + fn, "r") as file:
        for line in file:
            if line[0] == 'e':
                nodes = [int(s) for s in line.split() if s.isdigit()]
                node1 = nodes[0]
                node2 = nodes[1]
                adjacency_list.setdefault(node1, []).append(node2)
                adjacency_list.setdefault(node2, []).append(node1)
    file.close()


def get_candidates(clique):
    adjacency_sets = []
    for node in clique:
        adjacency_sets.append(set(adjacency_list.get(node)))
        #build list of all nodes common to all adjacency list of node
    return list(set.intersection(*adjacency_sets))


def find_maximal(heuristic):
    clique = []
    initial_node = rand.randrange(0, len(adjacency_list))
    candidates = adjacency_list.get(initial_node) #list of nodes (ints) attached to initial_node
    clique.append(initial_node) #append chosen node to clique
    while len(candidates) > 0:
        if heuristic:
            max_node = candidates[0]
            size = len(adjacency_list.get(candidates[0]))
            for node in candidates:
                temp = len(adjacency_list.get(node))
                if temp > size:
                    size = temp
                    max_node = node
            clique.append(max_node)
        else:
            clique.append(candidates[rand.randrange(0, len(candidates))])
        #rebuild candidates list
        candidates = get_candidates(clique)
    return len(clique)

#----------------------------------------------------#
adjacency_list = {}
fn = ("brock800_1.clq")
#fn = ("brock800_2.clq")
#fn = ("brock800_3.clq")
#fn = ("brock800_4.clq")
#fn = ("C2000.9.clq")
#fn = ("C4000.5.clq")
#fn = ("MANN_a45.clq")
#fn = ("p_hat1500-1.clq")
print("Selected file: ", fn)
initialise_graph()
print("Now that we've read in the graph")
num_tries = 0
max = 0
times = []
mean_score = []
max_trials = int(input("Input number of trials: "))
while num_tries < max_trials:
    try:
        start_time = time.time()
        print(num_tries + 1)
        #True = heuristic
        #False = without heuristic
        temp = find_maximal(True)
        mean_score.append(temp)
        times.append(time.time() - start_time)
        if temp > max:
            max = temp
    except Exception as e:
        print(e)
        pass


    num_tries += 1

print("Maximal clique: ", max)
print("Mean maximal clique found: ", round(np.mean(mean_score), 2))
print("Mean time for trials: ", round(np.mean(times), 4), "seconds")

#TO check adjacency list is correct
#print("Number of Nodes: ", len(adjacency_list))
#edge_count = 0
#for node in adjacency_list:
    #edge_count += len(adjacency_list.get(node))
#print("Number of Edges: ", edge_count//2)