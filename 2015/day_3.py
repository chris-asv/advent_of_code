# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

#     > delivers presents to 2 houses: one at the starting location, and one to the east.
#     ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

import pandas as pd

#load input
input_ = open('input_day_3.txt').readlines()[0]

print(input_[:10])

# Start point
nodos = [(0,0)]

# Rules:
def movementRules(node, step):
    rules = {"^": (node[0]+1, node[1]),
             "v": (node[0]-1, node[1]),
             ">": (node[0], node[1]+1),
             "<": (node[0], node[1]-1)}
    return rules[step]

print(nodos[-1])
# Apply rules
for step in input_:
    nodos.append(movementRules(nodos[-1], step))

serie_nodos = pd.Series(nodos, name="nodes")

print(serie_nodos.nunique())
print(serie_nodos.shape)

# --- Part Two ---

# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

#     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
print("--- Part Two ---")

# Start pointm
nodos_s = [(0,0)]
nodos_r = [(0,0)]

for k, step in enumerate(input_):
    if (k+1)%2 == 0:
        nodos_s.append(movementRules(nodos_s[-1], step))
    else:
        nodos_r.append(movementRules(nodos_r[-1], step))

serie_nodos_s = pd.Series(nodos_s, name="nodes")
serie_nodos_r = pd.Series(nodos_r, name="nodes")

serie_nodes_2 = pd.concat([serie_nodos_s, serie_nodos_r], axis=0)

print(serie_nodes_2.nunique())
print(serie_nodes_2.shape)