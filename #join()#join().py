#join()#join()
    
    
l=["this","is","kumar"]
j="$#".join(l)
print(j)


#changing case of string
s="this ia kumar"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize()) 

s= "hi shiva"
print(s.swapcase())

s=" naveen"
print(s.swapcase())

#type to check char present in the string
# is alnum
print("ABCabc123".isalnum())
print(" ABCabc123 ".isalnum())
#is  alpha
print("abcABC".isalpha())
print("ABC123".isalpha())
#is digit()
print("0123456789".isdigit())
print("012345678  abe ".isdigit())
#is uupper()
print("ABCDEFGH".isupper())
print("abcdefh123".isupper())
#islower()
print(" abcdefgh ".islower())
print("Abc123".islower())
#is tittlecase()
print("Ram Rao".istitle())
print("ram Rao".istitle())
#isspace
print(" ".isspace())
print("naveen".isspace())