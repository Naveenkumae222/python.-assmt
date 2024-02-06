#python assinment.py
# display number from a list usin loop

number=[1,2,3,4,5,6,7,8,9]
for i in number:
    print (i)


#print list in revese order using loop
mylist=[10,25,30,45,60,70,85]
newlist=[]
for i in range(1,len(mylist)+1):

    newlist.append(mylist[-i])
print(newlist)


#revese a given interger number
n=int(input("enter a number:"))
while n>0:
    r=n%10
    print(r,)
    n=n//10


