# --- Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

#     turn on 0,0 through 999,999 would turn on (or leave on) every light.
#     toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#     turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

# After following the instructions, how many lights are lit?

# Imports:
import pandas as pd
import numpy as np

# Data:
input_ = open("input_day_6.txt").readlines()

#Parse
parse_ = []
for j in input_:
    i = [k.replace("\n", "") for k in j.split(" ")]
    i.insert(1,None) if len(i) == 4 else None
    parse_.append(i)

# DF
parse_df = pd.DataFrame(parse_, columns=["task1", "task2", "star_point", "blabla", "end_point"])

# Veo
#parse_df.head()

# Grid with lights all turned off
grid = np.zeros((1000,1000))

def rectangle_grid(star_point, end_point):
    ij_ = []
    i_s, j_s = star_point
    i_e, j_e = end_point
    for i in range(i_s, i_e+1):
        for j in range(j_s, j_e+1):
            ij_.append((i,j))
    return np.array(ij_)

def task(grid, star_point, end_point, task):
    star_point = (int(k) for k in star_point.split(","))
    end_point = (int(k) for k in end_point.split(","))
    # DEfino rectangulo
    rectangle = rectangle_grid(star_point, end_point)
    # Aplico tarea
    for i, j in rectangle:
        grid[i,j] = 1 if task == "on" else (
                    0 if task == "off" else (
                    1 if grid[i,j] == 0 else 0))
    return grid

# Aplico reglas
for x in parse_df[["star_point", "end_point","task2"]].values:
    grid = task(grid, *x)

# How many lights are lit?
print(grid.sum())

# --- Part Two ---

# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

#     turn on 0,0 through 0,0 would increase the total brightness by 1.
#     toggle 0,0 through 999,999 would increase the total brightness by 2000000.
print("--- Part Two ---")

def task2(grid, star_point, end_point, task):
    star_point = (int(k) for k in star_point.split(","))
    end_point = (int(k) for k in end_point.split(","))
    # DEfino rectangulo
    rectangle = rectangle_grid(star_point, end_point)
    # Aplico tarea
    for i, j in rectangle:
        grid[i,j] = grid[i,j] + 1 if task == "on" else (
                   (grid[i,j] - 1 if grid[i,j] - 1 >= 0 else 0
                   ) if task == "off" else grid[i,j] +2)
    return grid

grid = np.zeros((1000,1000))

# Aplico reglas
for x in parse_df[["star_point", "end_point","task2"]].values:
    grid = task2(grid, *x)

# How many lights are lit?
print(grid.sum()) 