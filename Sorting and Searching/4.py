#Merge Sort
def merge(left,right):
    lis1=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if (left[i]<=right[j]):
            lis1.append(left[i])
            i+=1
        else:
            lis1.append(right[j])
            j+=1
    lis1 += left[i:]
    lis1 += right[j:]
    return lis1

def mergesort(lis):
    if len(lis)<=1:
        return lis
    mid=int(len(lis)/2)
    left=mergesort(list(lis[:mid]))
    right=mergesort(list(lis[mid:]))
    return merge(left,right)
lis=[-3,5,1,0,8,-14,16]
print(mergesort(lis))