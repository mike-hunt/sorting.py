def swap(alist, index):
    
    a = alist[index] 
    b = alist[index+1]
    alist[index] = b
    alist[index+1] = a
    return (alist)

def bsort(alist):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(alist)-1):
            if (alist[i] > alist[i+1]):
                alist = swap(alist, i)
                swaps = True
    return (alist)

def mini(alist):
    answer = alist[0]
    for item in alist:
        if item< answer:
            answer = item
    return (answer)

def ssort(alist):
    blist = []
    while len(alist >0):
        N = mini(alist)
        alist.remove (N)
        blist.append(N)
    return (blist)

    
def mergeSort(alist)
   
 
    return result
