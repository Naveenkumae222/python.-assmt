

vowels=['a','e','i','o','u']
word = input("enter word:").split()
unique_vowels=set()

for word in word:
    for char in word.lower():
        if char in vowels:
         unique_vowels.add(char)

print("unique",unique_vowels)