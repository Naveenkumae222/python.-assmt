#strip function.py
city=input("enter the city name")
list=["khammam","palvancha","kothagudem","manugur"]

if city.strip() in list:
    print ("yes it is avallable")
else:
    print(city, "not avalable")
  

#lstrip
a = " !!!!hh   hello world "
print(a.lstrip())


#rstrip
a = "hello world    "
print(a.rstrip(), end="")
print(5)