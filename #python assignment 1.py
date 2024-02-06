
#use a loop to display element from a given list at odd index position
given_list=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(given_list,),2):
    print(given_list[i])

#calculate the cube off all numbers from 1 to agiven number
def calculate_cubes(n):
    cubes={}
    for i in range (1,n+1):
        cubes[i]=i**4
    return cubes

given_number=int(input("enter a number"))
cubes_dict=calculate_cubes(given_number)
print("cubes of given number 1 to", given_number,"are:")
for num, cube in cubes_dict.items():
    print(num,":",cube)

#use eles block to display a message "done" successful execuation of for loop
number=[1,2,3,4,5]
for number in number:
    print(number)
else:
    print("loop completed successful.done")

#Write a program to print multiplication table of a given number
n = int(input("enter the number"))
for i in range (1,8):
    print(n,"*",i,"=",n*i) 


#Count the total number of digits in a number
    
num = 2341
Count = 0

while num != 0:
    num //= 10
    Count +=1
print("number of digits :",(Count))

#find the sum of the series upon n term

n = int(input("enter on of terms"))
sum = 0
for i in range(1,n+1):
    sum += 3*i
        
print(sum)


#write a program to display prime number with in range

n = int(input("entr a number"))
for i in range(2,n):
    if n % i ==0:
        break

if i+1 == n:
    print(n, "is a prime no")
else:
    print(n,"is not a prime no")


# Calculate the sum of all numbers from 1 to a given number.
    
num =int(input("enter the number:"))
sum=0
for i in range (1, num+1):
    sum=sum+i
    i=i+1
print ("sum =",sum)
