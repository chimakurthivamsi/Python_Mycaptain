myList=[]
list1=[]
n=int(input("Enter the number of terms:"))
for i in range (n):
    myList.append(int(input()))
print(myList)
for i in myList:
    if int(i)>0:
        list1.append(i)
s=str(list1)[1:-1]
print(s)
