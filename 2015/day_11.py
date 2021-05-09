# --- Day 11: Corporate Policy ---

# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

#     Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
#     Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
#     Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

# For example:

#     hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
#     abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
#     abbcegjk fails the third requirement, because it only has one double letter (bb).
#     The next password after abcdefgh is abcdffaa.
#     The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

# Given Santa's current password (your puzzle input), what should his next password be?


# first_requirement
abc_list = list(map(chr, range(97, 123)))
abc_string = list(map(lambda x: "".join(x),zip(abc_list[:-1], abc_list[1:], abc_list[2:])))
pairs_list = ["".join([i,i]) for i in abc_list]


# Some custom functions
def ord_custom(character):
    """
    from a lower case a,b,c,... 
    return a number between 0 and 25
    where a is maped to 0 and z to 25
    """
    if character in abc_list:
        return ord(character) - ord('a')
    else:
        raise ValueError("not lowercase")

def chr_custom(number):
    """
    from a nuber between 0 and 25 
    return a character
    where 0 is maped to a and 25 to z
    """
    if number in range(ord('z') - ord('a') + 1):
        return chr(number + ord('a'))
    else:
        raise ValueError("integer must be between 0 and 25")

def always_btw_0_25(number, carry=0):
    """
    from each positive number >= 0 
    return a mapping to the range 0 to 25
    where after 26 map to 0 , 27 map to 1 and so on
    and also the number of times that 25 fits in number completely
    """
    if number < 0 :
        raise ValueError("number must be positive")
    elif 0 <= number <= 25:
        return number, carry
    else:
        carry = carry + 1
        return always_btw_0_25(number - 26, carry)

# for i in range(52):
#     print(chr_custom(always_btw_0_25(i)))

def validate_len_str(string):
    """
    The first rule: string lenght 8
    """
    if type(string) == str:
        return len(string) == 8
    else:
        raise TypeError("is not a string")

def validate_lowercase(string):
    """
    the second rule: string in lowercase
    """
    try:
        return string.islower()
    except:
        raise TypeError("is not a string")

def get_list_vals_of_str(string):
    """
    from a valid string (len 8 & lowercase)
    return the value of each character in a vector
    """
    if validate_len_str(string) & validate_lowercase(string):
        return [ord_custom(s) for s in string]
    else:
        raise TypeError("Is not a lowercase string with lenght 8")

def get_next_vector(vector):
    """
    return the next vector after add 1
    base = 25
    len(vector) == 8
    """
    val , carry = always_btw_0_25(vector[7]+1)
    vector[7] = val
    for i in range(6,-1,-1):
        val , carry = always_btw_0_25(vector[i]+carry)
        vector[i] = val
    return vector

def get_next_string(string):
    vector = get_list_vals_of_str(string)
    next_v = get_next_vector(vector)
    return "".join(map(chr_custom,next_v))

def validate_iol(string):
    if len(set(["i","o","l"]) & set(list(string))) == 0:
        return True
    else:
        return False 

def validate_abc(string):
    for abc in abc_string:
        if abc in string:
            return True
        else:
            pass
    return False

def validate_2pairs(string):
    pair_1 = None
    pair_2 = None
    for i, aa in enumerate(pairs_list):
        if (aa in string) & (pair_1 == None):
            pair_1 = aa
        elif (aa in string) & (pair_2 == None):
            pair_2 = aa
    # Retun
    if (pair_1 != None) & (pair_2 != None):
        return True
    else:
        return False
        
def get_next_new_password(string):
    next_string = get_next_string(string)
    # Validate the new rules
    while (validate_iol(next_string) &\
           validate_abc(next_string) &\
           validate_2pairs(next_string)) != True:
        next_string = get_next_string(next_string)
    return next_string

# # It works 
# In [202]: string = 'abcdefgh'
# In [203]: get_next_new_password(string)
# Out[203]: 'abcdffaa'

# # It works 
# In [204]: string = 'ghijklmn'
# In [205]: get_next_new_password(string)
# Out[205]: 'ghjaabcc'

input_ = open(file="input_day_11.txt", mode='r').read()
next_new_password = get_next_new_password(input_)
print(next_new_password)

# --- Part Two ---
# Santa's password expired again. What's the next one?

next_new_password2 = get_next_new_password(next_new_password)
print(next_new_password2)

