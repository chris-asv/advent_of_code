# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

import pandas as pd
vowels = "aeiou"
abc_ = "abcdefghijklmnopqrstuvwxyz"
aabbcc_ = [i*2 for i in abc_]
#ab_cd = [abc_[i:i+2] for i in range(len(abc_)-1)]
ab_cd = ["ab", "cd", "pq", "xy"]

series_text = pd.read_csv("input_day_5.txt", header=None, names=["text"])

def flg_3vowels(string):
    return len(list(filter(lambda x: x in vowels, list(string)))) >= 3

def flg_twice(string):
    pairs_in_str = [string[i:i+2] for i in range(len(string)-1)]
    return len(list(filter(lambda x: x in aabbcc_, pairs_in_str))) >= 1

def flg_ab_cd(string):
    pairs_in_str = [string[i:i+2] for i in range(len(string)-1)]
    return len(list(filter(lambda x: x in ab_cd, pairs_in_str))) == 0

def nice_string(string):
    return flg_3vowels(string) + flg_twice(string) + flg_ab_cd(string) == 3

total_nice_strings = sum(list(map(nice_string, series_text.text.values)))

print(total_nice_strings)

# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

print("--- Part Two ---")

def flg_pairs(string):
    pairs_in_str = [string[i:i+2] for i in range(len(string)-1)]
    max_index = len(pairs_in_str) - 1
    i = 0
    while i <= (max_index - 2):
        if pairs_in_str[i] in pairs_in_str[i+2:]:
            return True
        i +=1
    return False

def flg_xyx(string):
    three_leters = [string[i:i+3] for i in range(len(string)-2)]
    for i in three_leters:
        if (i[0] == i[2]):
            return True
    return False

def super_nice_string(string):
    return flg_pairs(string) + flg_xyx(string) == 2

print(series_text.text.apply(lambda x: super_nice_string(x)).sum())