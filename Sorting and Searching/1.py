#Bubble Sort
arr=[2,5,3,1,8,4]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)


