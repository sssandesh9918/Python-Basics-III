#Tower of Hanoi
def TowerOfHanoi(n,s,d,a): 
    if n==1: 
        print ("Move disk 1 from source %s to destination %s"%(s,d))
        return
    TowerOfHanoi(n-1,s,a,d) 
    print("Move disk %d from source %s to destination %s"%(n,s,d))
    TowerOfHanoi(n-1,a,d,s) 
n = 3
TowerOfHanoi(n,'A','B','C')