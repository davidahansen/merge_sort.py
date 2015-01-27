import sys

def merge_sort(li, c):
    if len(li) < 2: return li 
    m = len(li) / 2 
    return merge(merge_sort(li[:m],c), merge_sort(li[m:],c),c) 

def merge(l, r, c):
    result = []
    while l and r:
        s = l if l[0] < r[0] else r
        result.append(s.pop(0))
        if (s == r): c[0] += len(l)
    result.extend(l if l else r)
    return result

with open(sys.argv[1]) as f:
    data = []
    for line in f:
        x = int(line)
        #print x
        data.append(x)

count = [0]
merge_sort(data, count)
print "inversion count is " + str(count[0])