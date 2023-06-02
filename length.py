#program to print even length words in a string
f = []
def length(s):
    l = s.split(" ")
    for i in l:
        if len(i) % 2 == 0:
            f.append(i)
    print(' '.join(f))
length("i am python")