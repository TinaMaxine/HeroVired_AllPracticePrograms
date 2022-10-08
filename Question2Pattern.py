#Question 2 : Write a python program to print the pattern of number as given below:
"""
Output:
0
0 1
0 1 2
0 1 2 3

"""
num=int(input("Enter the number of lines for your pattern: "))#input 4
for i in range(1,num+1):
    for j in range(i):
        print(j,end="")
        print(" ",end="")
    print()
