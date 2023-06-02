#to find smallest and largest number in a list
p = [8, 9, 25, 39, 45, 6]
def swap(a, b):
    temp = p[a]
    p[a] = p[b]
    p[b] = temp
for i in range(len(p)):
    for j in range(1, len(p)-i):
        if p[j] < p[j-1]:
            swap(j, j-1)
print("Smallest number",p[0])
print("Largest number ",p[5])