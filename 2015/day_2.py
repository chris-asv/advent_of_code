# --- Day 2: I Was Told There Would Be No Math ---

# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

# For example:

#     A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
#     A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

# Import pandas
import pandas as pd

#load input
boxes_list = pd.read_csv("input_day_2.txt", header=None)\
               .rename(columns={0:"l_w_h"})

def area_by_box(l_w_h_str):
    # split the measures:
    w,h,l = [int(m) for m in l_w_h_str.split("x")]
    list_m = np.array([w*h, w*l, h*l])
    area = sum(list_m*2) + min(list_m)
    return area

# Obtqain the area
boxes_list["total_area"] = boxes_list.l_w_h.apply(lambda x: area_by_box(x))

total = boxes_list.total_area.sum()
print(total)

# The first half of this puzzle is complete! It provides one gold star: *
# --- Part Two ---

# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

# For example:

#     A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
#     A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

# How many total feet of ribbon should they order?

def ribbon_by_box(l_w_h_str):
    # Split the measures:
    list_m = [int(m) for m in l_w_h_str.split("x")]
    # Obtain the ribbon for the bow
    ribbon_bow = np.prod(list_m)
    # Remove the max value
    list_m.remove(max(list_m))
    # Ribbon to wrap the present
    ribbon_wrap = sum(list_m)*2
    return ribbon_bow + ribbon_wrap

# Obtain the total ribbon
boxes_list["total_ribbon"] = boxes_list.l_w_h.apply(lambda x: ribbon_by_box(x))

# Total
print(boxes_list.total_ribbon.sum())