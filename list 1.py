l=list(range(1,10,2))
print(l)


l=list(range(1,40,3))
print(l)

l=list(range(-1,-100,-4))
print(l)


l=list(range(3,-50,-2))
print(l)


l=list(range(-2,-100,-3))
print(l)
####

l=[10,20,30,[40,50,60],70,80,90,100]
print(l[3])


l=[10,20,30,[40,50,60],70,80,90,100]
for i, sublist in enumerate(l):
    if isinstance(sublist,list) and sublist:
        print(sublist[-1], end=" ")
        print(l[i+1])

l=[10,20,30,[40,50,60],70,80,90,100]
for i, sublist in enumerate(l):
    if isinstance(sublist,list) and sublist:
        print(sublist[-2], end=" ")
        print(l[i+1])


l=[10,20,30,[40,50,60],70,80,90,100]
for i, sublist in enumerate(l):
    if isinstance(sublist,list) and sublist:
        print(sublist[-3], end=" ")
        print(l[i+1])


l=[10,20,30,[40,50,60],70,80,90,100]
for i, sublist in enumerate(l):
    if isinstance(sublist,list) and sublist:
        print(sublist[-2], end=" ")
        print(l[i+3])





l=[10,20,30,40,50,60,70,]
for i in l:
    print(i)

l=[30,40,50,60,70,]
for i in l:
    print(i)


l=[-10,20,30,40,50,-60,70,]
for i in l:
    print(i)


#len(list)
l=[10,20,30,40,60,[1+2],30]
print(len(l))

l=(1234567,34567,34568,)
print(len(l))

#count
l=[10,20,30,40,50]
print(l.count(20))

l=[23,34,56,78,45,34,56,123,23,34,65]
print(l.count(23))


#index
l=[1,2,3,4,5,6,7]
print(l.index(4))
l=[10,20,30,40,50,60,78]
print(l.index(78))
l=[23,45,67,84,-12,34,-45,]
print(l.index(-12))


#l.append
l=[]
l.append(10)
l.append(20)
print(l)


l=[]
l.append(23)
l.append(20)
l.append(35)
l.append(60)
print(l)

l=[ 11,6]
l.append(123)

print(l)

#l.insert
l=[10,20,30,40,50]
l.insert(3,222)
print(l)

l=[12,34,56,67,98]
l.insert(1,100)
print(l)

l=[1,2,3,4,5,6,7,8,9]
l.insert(9,10)
print(l)

#extend()
l1=["bike","car","auto"]
l2=["bus","train"]
l1.extend(l2)
print(l1)
print(l2)


l1=["bike","car","auto"]
l2=["bus","train"]
l1.extend("flight")
print(l1)
print(l2)

#l.remove
l1=[10,2,40,34,50,78]
l1.remove(34)
print(l1)

l1=["ramu","shiva","kumar"]
l1.remove("kumar")
print(l1)


#pop
l1=[11,23,34,45,56,78]
print(l1.pop())

l1=[11,23,34,45,56,78]
print(l1.pop(4))

l1=[11,23,34,45,56,78]
print(l1.pop(5))


#reverse()
l=[10,20,30,40,50,60,]
l.reverse()
print(l)

l=[10,20,30,40,50,60,90,80,70,100,200,250]
l.reverse()
print(l)

#sort()
l=[10,20,30,200,250,60,70,90,80,150]
l.sort()
print(l)

l=[10,20,30,300,4564,200,250,60,70,90,80,150]
l.sort()
print(l)

#compare string()
name1 = "KUMAR"
name2 = "kumar" 

if name1.casefold() == name2:
    print("it is match")
else:
    print("do not match")

name1 = "kumar"
name2 = "Kumar"
print(name1 ==name2)

name1 = "kumar"
name2 = "Kumar"
print(name1 >=name2)


#nested list
x=[[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]]
for i in x:
    print(i)
print("elements in matrix style")
for i in range(len(x)):
    for j in range (len(x[i])):
        print(x[i][j],end=" ")
    print()

x=[[12,23,34,45],[23,34,45,56],[45,56,67,68]]
for i in x:
    print(i)
print("elemenrs in martix style")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print()


#print odd number in the range of 0 to 30 
for num in range(1,31,2):
    print(num)

#print even number in range of 0 to 30
for num in range(0,30,2):
    print(num)

#list comperhensive
l=[2*1,2*2,2*3,2*4,2*5]
l1=[]
for x in l:
    l1.append(x*x)
print(l1)

l=[3*1,3*2,3*3,3*4]
l1=[]
for x in l:
    l1.append(x*x)
print(l1) 

#compare string elements by usig sort
l=["apple","orange","watermelon"]
l.sort()
print(l)

words=["balaya","shafi","chiru"]
output=','.join(word[0] for word in words)
print(output)