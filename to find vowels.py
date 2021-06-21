print("To find the number of vowles in a given string")
count = 0
string=input("enter the string:")
for i in string:
    if i in "aeiouAEIOU":
        count=count+1
        print("the vowels in the given string are:",i)
print("the total numbr of vowles are:",count)
