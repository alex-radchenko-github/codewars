def arrayRankTransform(arr):
    rez = {}
    for i in sorted(arr):
        rez.setdefault(i, len(rez) + 1)
    return map(rez.get, arr)
#print(arrayRankTransform([40,10,20,30]))
#print(arrayRankTransform([100,100,100]))
print(arrayRankTransform([37,12,28,9,100,56,80,5,12]))#[5,3,4,2,8,6,7,1,3]