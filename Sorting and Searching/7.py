#Interpolation Search
def interpolationsearch(a,element):
    l=0
    r=len(a)-1
    while(l<=r):
        mid=int(l+float(((r-l)/(a[r]-a[l])))*(element-a[l]))
        if a[mid]==element:
            return mid
        elif a[mid]<element:
            l=mid+1
        else:
            return mid
    return -1
a=[1,5,6,7,13,19,26,33,48]
element=int(input("Enter the element you want to search"))
re=interpolationsearch(a,element)
if re!= -1: 
    print("Element is present at index", re)
else: 
    print("Element is not present in array") 