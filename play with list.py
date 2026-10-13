L = [5, 4, 6, 9, 2, 8, 1, 3, 10, 7]
print ("Orginal List :",L)

count = 0

for i in L:
    count += 1

avg = count/len(L)

print ("sum =", count)
print ("avg =", avg)

L.sort()

print ("Smallest element is", L[0])
print ("Largest element is", L[-1])