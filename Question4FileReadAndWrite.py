#Reading the file by line
# fob=open("Practise/myFile.txt","a")
# print("line",fob.readline())
# fob.close()
#Reading the file
fob=open("Practise/myFile.txt","r")
print("File contains:\n")
print(fob.read())
print("\n")
fob.close()
Append=input("Do you want to append your file? Yes or No (Y/N): ")#Appending the file
if(Append=="Y"):
    addStringsToTheFile=input("Please make changes here: ")
    fob=open("Practise/myFile.txt","a+")
    fob.write(addStringsToTheFile)
    fob.close()
    fob=open("Practise/myFile.txt","r")
    print(fob.read())
    fob.close()
OverWrite=input("Do you want to overwrite the existing file? Yes or No (Y/N): ")#Overwriting the file
if(OverWrite=="Y"):
    addStringsToTheFile=input("Please make changes here: ")
    fob=open("Practise/myFile.txt","w+")
    fob.write(addStringsToTheFile)
    fob.close()
    fob=open("Practise/myFile.txt","r")
    print(fob.read())
    fob.close()


    