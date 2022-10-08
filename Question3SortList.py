"""Question 3 :Write a python program to sort a list in ascending order.
List =[2,4,1,3]
sortedList =[1,2,3,4]"""
List=[2,4,1,3]
SortedList=[]
for k in range(len(List)):
    for i in List:
        min=0
        flag=False
        for j in List:
            if(i<=j):
                flag=True
            else:
                flag=False
                break
        if(flag==True):
            #print(i)
            min=i
            #print(min)
            SortedList.append(min)
            List.remove(min)
            #print(List)
print(SortedList)




        
