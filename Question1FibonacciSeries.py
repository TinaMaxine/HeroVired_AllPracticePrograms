#Fibonacci series within a given range
def myFibonacci(givenRange):
    n=0
    m=1
    sum=0
    while(n<=givenRange):
        print(n)
        sum=n+m
        n=m
        m=sum

myFibonacci(givenRange=int(input("Enter the range for Fibonacci series ")))