order = 5

scalar = [i for i in range(order) if i != 0]
c_scalar = [i for i in range(order)]

lines = [(i, j) for i in range(order) for j in range(order) if (i, j) != (0, 0)]

equ_class = []
for (a1, b1) in lines:
    tally = 0
    test = []
    for s in scalar:
        if ((a1*s)%order, (b1*s)%order) not in equ_class:
            tally += 1
        else:
            test.append([s, (a1, b1), ((a1*s)%order,(b1*s)%order)])
            break;
    if tally == len(scalar):
        equ_class.append((a1, b1))

print lines
print len(lines)
print equ_class

equ_class = [(a, b, c) for (a, b) in equ_class for c in c_scalar]
print equ_class