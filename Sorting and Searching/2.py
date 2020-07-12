#Insertion sort
li=[2,5,3,1,8,4]
for i in range(1,len(li)):
    k=li[i]
    j=i-1
    while(j>=0 and li[j]>k):
        li[j+1]=li[j]
        j=j-1
    li[j+1]=k
print(li)   