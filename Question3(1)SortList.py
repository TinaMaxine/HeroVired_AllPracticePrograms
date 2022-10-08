List=[2,4,1,3]
def mySortingArray():
    for i in range(4):
        for j in range(i+1,4):
            temp=0
            if(List[i]>List[j]):
                temp=List[i]
                List[i]=List[j]
                List[j]=temp
    print(List)
mySortingArray()