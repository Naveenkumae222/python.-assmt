# arthemetic operators +,-,/,*,%
a=45
b=64
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)

# comparision operators >,<,==
print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
#logical operators  and,or,not
print(a and b<a)
print(a<b or b<a)
print(not (a>b and b<a))


#compound operator
a=23
a&=16
print(a)
a=43
a*=13
print(a)
a=34
a-=67
print(a)
a=57
a+=87
print(a)
a=45
a%=12
print(a)



#identity operator
a=20
b=20
print(a is b)

a=34
b=56
print(a is not b)

a=[45,67,89,67,]
b=[34,67,87,65]
print(b is a)

#membership operator

l=[34,56,85,98,]
print(56 in l)

l=[10,57,74,89,56]
print(77 in l)

a=[77,89,67,23,45,]
print(-67 in a)


#input and ouput statments 

a= int(input('enter the first number:'))
b= int(input('enter the sec number:'))
print(type(a))
print(type(b))
print(a+b)


