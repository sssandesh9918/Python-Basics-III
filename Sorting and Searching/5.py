#Linear Search
a=[2,5,6,15,23,62,52,8]
element=int(input("Enter the element you want to enter"))
for i in range(len(a)):
    if a[i]==element:
        print("Element is present in %d"%(a.index(element)))
        break
    if i==len(a)-1:
        print("It is not present")

#pythonic
a=[2,5,6,15,23,62,52,8]
element=int(input("Enter the element you want to enter"))
if element in a:
    print("Element is present in %d"%(a.index(element)))
else:
    print("not present")
