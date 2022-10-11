#1
import numbers


def TF():
    numb = [10, 20, 30, 40, 10]
    print("Yes") if numb[0] == numb[-1] else print("No")

#2
def return_count(string,word):
    string=string.lower() 
    return string.count(word)
 
string2="Python is a high-level, general-purpose programming language. Python is dynamically-typed and garbage-collected"
return_count(string2,'python')

#3
x = int(input("User Input: "))
count_of_digits = 0
while x > 0:
   x = int(x/10)
   count_of_digits += 1
print("Number of Digits: ",count_of_digits)

#4
l = -10
u = 5
if l%2==0:
    for num in range(l, u + 1, 3):
        print(num)
else:
    for num in range(l+1, u + 1, 3):
        print(num)