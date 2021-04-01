# --- Day 7: Some Assembly Required ---

# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

#     123 -> x means that the signal 123 is provided to wire x.
#     x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
#     NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

input_ = [line.replace("\n", "")\
              .split(" -> ") for line in open("input_day_7.txt").readlines()]
lines_ = {l[1]:l[0].split(" ") for l in input_}

bit_op = {"AND": lambda x,y: x & y,
          "OR": lambda x,y: x | y,
          "RSHIFT": lambda x,y: x >> y,
          "LSHIFT": lambda x,y: x << y,
          "NOT": lambda x: ~ x & (2**16 - 1)
          }

wires = {}

def find_signal(wire):
    try:
        # If wire has been already defined
        print(wire, wires)
        return int(wires[wire])
    except:
        print(f"No exise {wire}")
        # If wire is defined by one element
        if len(lines_[wire]) == 1:
            print("Sólo hay un elemento")
            try:
                # If the element is a number
                wires[wire] = int(lines_[wire][0])
                print(f"Se añade '{wire}' directo de Lines")
                find_signal(wire)
            except:
                # If the element is another wire in lines_
                print(f"Se añade '{wire}' mediante proceso")
                wires[wire] = find_signal(lines_[wire][0])
                find_signal(wire)
        # If there are two elements, always is a 'NOT' binary operation:
        elif len(lines_[wire]) == 2:
            print("Hay dos elementos")
            try:
                print("Intenta ver si existe ya en wires")
                wires[wire] = bit_op["NOT"](wires[lines_[wire][1]])
                find_signal(wire)
            except:
                print(f"No existe, generalo y entonces ya creas {wire}")
                find_signal(lines_[wire][1])
                wires[wire] = bit_op["NOT"](wires[lines_[wire][1]])
                find_signal(wire)
        else:
            print("Hay 3 elementos")
            if lines_[wire][1] in ["LSHIFT", "RSHIFT"]:
                print("La operacion es R-L SHIFT")
                int_shift = int(lines_[wire][2])
                try:
                    print("Si ya existe, intentalo")
                    wires[wire] = bit_op[lines_[wire][1]](wires[lines_[wire][0]], int_shift)
                    find_signal(wire)
                except:
                    print("No existe, crealo")
                    find_signal(lines_[wire][0])
                    wires[wire] = bit_op[lines_[wire][1]](wires[lines_[wire][0]], int_shift)
                    find_signal(wire)
            else:
                print(f"La operacin es {lines_[wire][1]}")
                if (lines_[wire][0] and lines_[wire][2]) in wires.keys():
                    print("ambos estan en keys")
                    wires[wire] = bit_op[lines_[wire][1]](wires[lines_[wire][0]],wires[lines_[wire][2]])
                elif (lines_[wire][0] or lines_[wire][2]) in wires.keys():
                    print("Solo hay uno, indentifico el que no está")
                    i_x = 2 if lines_[wire][0] in wires.keys() else 0
                    if lines_[wire][i_x].isdigit():
                        print("El que no está es digito")
                        wires[wire] = bit_op[lines_[wire][1]](int(lines_[wire][i_x]),wires[lines_[wire][2]])\
                         if i_x == 0 else bit_op[lines_[wire][1]](wires[lines_[wire][0]],int(lines_[wire][i_x]))
                        find_signal(wire)
                    else:
                        print("El que  no está no es digito")
                        print(f"Genero {lines_[wire][i_x]}")
                        find_signal(lines_[wire][i_x])
                        print(f"Genero {wire}")
                        wires[wire] = bit_op[lines_[wire][1]](wires[lines_[wire][i_x]],wires[lines_[wire][2]])\
                         if i_x == 0 else bit_op[lines_[wire][1]](wires[lines_[wire][0]],wires[lines_[wire][i_x]])
                        find_signal(wire)
                else:
                    print("No hay ninguno")
                    if lines_[wire][0].isdigit():
                        print("El priemro es digito")
                        find_signal(lines_[wire][2])
                        wires[wire] = bit_op[lines_[wire][1]](int(lines_[wire][0]),wires[lines_[wire][2]])
                    elif lines_[wire][2].isdigit():
                        print("El segundo es digito")
                        find_signal(lines_[wire][0])
                        wires[wire] = bit_op[lines_[wire][1]](wires[lines_[wire][0]], int(lines_[wire][2]))
                    else:
                        print("Ninguno es digito")
                        find_signal(lines_[wire][0])
                        find_signal(lines_[wire][2])
                        wires[wire] = bit_op[lines_[wire][1]](wires[lines_[wire][0]],wires[lines_[wire][2]])
                        find_signal(wire)

find_signal('a')

print(wires['a'])

# --- Part Two ---

# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

print('--- Part Two ---')
wires = {}
find_signal('a')
print(wires['a'])

wires = {'b' : wires['a']}

find_signal('a')
print(wires['a'])
