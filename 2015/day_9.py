# --- Day 9: All in a Single Night ---

# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141

# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982

# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

# Loading input
input_ = open(file="input_day_9.txt", mode="r").read().splitlines()
# TRansform input
distances = [{"pair":i.split(" = ")[0].split(" to "),
              "distance":int(i.split(" = ")[1])} for i in input_]
# First, take tha min distance and the cityes
in_link = min(distances, key=lambda x: x["distance"])
# And save it here:
shorther_way = [in_link]
# Then remove that point of distances list
distances.remove(in_link)
# Split the nodes
nodeA, nodeB = in_link["pair"]

# To chose the shorthes next step
def find_agg_link(nodeA, nodeB, some_way, distances, agg_function=min):
    # initial pair
    ini_pair = [nodeA, nodeB]
    # Find the pair in which nodes are
    linksA = list(filter(lambda x: nodeA in x["pair"], distances))
    linksB = list(filter(lambda x: nodeB in x["pair"], distances))
    # Find the pair with the agg_function distance for each node
    aggA = agg_function(linksA, key=lambda x: x["distance"])
    aggB = agg_function(linksB, key=lambda x: x["distance"])
    # If the path close, then remothe that path
    if aggA == aggB:
        # Remove from links
        linksA.remove(aggA)
        linksB.remove(aggB)
        # Find the pair with the agg_function distance for each node
        aggA = agg_function(linksA, key=lambda x: x["distance"])
        aggB = agg_function(linksB, key=lambda x: x["distance"])
    # which of them is the shorter/longer?
    agg_ = agg_function([aggA, aggB], key=lambda x: x["distance"])
    # aparte the other one
    #_agg = agg_function([aggA, aggB], key=lambda x: -1*x["distance"])
    # And remove the oposit only if the intersection == 1
    #distances.remove(_agg) if len(set(aggA["pair"]) & set(aggB["pair"])) == 1 else None
    # shortest/longest pair:
    agg_pair = agg_["pair"]
    # Save it:
    some_way = some_way + [agg_]
    # The node that no longer interests
    linked_node = (set(ini_pair) & set(agg_pair)).pop()
    # Errase all the links in which the linked node apears
    distances = list(filter(lambda x: linked_node not in x["pair"], distances))
    # which node is active?
    newA, newB = list(set(ini_pair).union(set(agg_pair)) - set([linked_node]))
    return newA, newB, some_way, distances

# ini_pair = [newA, newB]
# nodeA, nodeB = ini_pair

while len(distances) > 1:
    nodeA, nodeB, shorther_way, distances = find_agg_link(nodeA, nodeB, shorther_way, distances)
    print(len(distances))

print("--- Part One ---")
print(sum([x["distance"] for x in shorther_way]))

# --- Part Two ---

# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?
print("--- Part Two ---")

# Loading input
input_ = open(file="input_day_9.txt", mode="r").read().splitlines()
# TRansform input
distances = [{"pair":i.split(" = ")[0].split(" to "),
              "distance":int(i.split(" = ")[1])} for i in input_]
# First, take tha max distance and the cityes
in_link = max(distances, key=lambda x: x["distance"])
# And save it here:
longer_way = [in_link]
# Then remove that point of distances list
distances.remove(in_link)
# Split the nodes
nodeA, nodeB = in_link["pair"]

while len(distances) > 1:
    print("=="*50)
    nodeA, nodeB, longer_way, distances = find_agg_link(nodeA, nodeB, longer_way, distances, agg_function=max)
    print(f"({nodeA}, {nodeB})")
    print(longer_way)
    print(len(distances))

print("It does not work for logest way")
print(sum([x["distance"] for x in longer_way]))

# [{'pair': ['Tristram', 'AlphaCentauri'], 'distance': 118},
#  {'pair': ['Norrath', 'Tristram'], 'distance': 142}, 
#  {'pair': ['Norrath', 'Arbre'], 'distance': 135}, 
#  {'pair': ['Arbre', 'Snowdin'], 'distance': 129}, 
#  {'pair': ['Snowdin', 'Straylight'], 'distance': 99}, 
#  {'pair': ['Tambi', 'Straylight'], 'distance': 70}, 
#  {'pair': ['Faerun', 'Tambi'], 'distance': 71}]

###########################################################
# Using brute force
###########################################################

# Imports
import itertools

# Loading input
input_ = open(file="input_day_9.txt", mode="r").read().splitlines()
# Transform input
distances = [{"pair":i.split(" = ")[0].split(" to "),
              "distance":int(i.split(" = ")[1])} for i in input_]
# Unique nodes:
unique_nodes = []
# For creating the bidirected path
all_distances = {}

for k in distances:
    # Unique nodes
    unique_nodes.extend(k["pair"])
    # Bidirected links
    pA, pB = k["pair"]
    dist = k["distance"]
    all_distances[(pA, pB)] = dist
    all_distances[(pB, pA)] = dist

# With a set, I keep the unique nodes
unique_nodes = set(unique_nodes)

# With unique nodes build avery permutation
permutations = itertools.permutations(unique_nodes)
# And then build the pairs in every path
all_paths = [zip(p[:-1], p[1:]) for p in permutations]
# Calculate all distances
total_distances = [sum([all_distances[pair] for pair in path]) for path in all_paths]

print(f"The shortest path measure: {min(total_distances)}")
print(f"The longest path measure: {max(total_distances)}")