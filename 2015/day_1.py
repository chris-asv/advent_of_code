
#load input
input = open('input_day_1.txt').readlines()[0]

#-------------#
# Pure python #
#-------------#

# Part 1: floor
#--------------
# Split the string input 
input_list = list(input)
# map to values 1 and -1
input_maped = map(lambda x: 1 if x=="(" else -1 if x==")" else None, input_list)
# make the sum
floor = sum(input_maped)
print(f"Go to floor: {floor}")

# Part 2: position
#-----------------

input_maped_list = list(input_maped)
input_m_l_cumsum = [sum(input_maped_list[:i+1]) for i in range(len(input_maped_list))]
position = input_m_l_cumsum.index(-1) + 1
print(f"Position is: {position}")

#--------#
# Pandas #
#--------#

# Import
import pandas as pd

# Part 1: floor
#--------------
# Create a serie
s = pd.Series(list(input), name="direction")
# count each character
s_count = s.value_counts()
# sum the counts
floor = s_count.loc['('] - s_count.loc[')']
print(f"Go to floor: {floor}")

# Part 2: position
#-----------------
# Transform to DataFrame
df = pd.DataFrame(s)
# Map the value
df["value"] = df.direction.apply(lambda x: 1 if x == "(" else -1 if x==")" else None)
# Create the cummulative sum of the values 
df["cumsum_v"] = df.value.cumsum()
# look for the rows with value equal to -1 and take the first of them
position = df.loc[df.cumsum_v == -1].iloc[0].name + 1
print(f"Position is: {position}")