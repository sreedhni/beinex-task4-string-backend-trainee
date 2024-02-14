str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  

str = "Hello World"
print(str[0])  

str = "Hello World"
print(str[2:5]) 

str = "Hello World"
print(len(str))  


str = "Hello World"
print(str.split()) 

string = "   Hello   "
print(string.strip())  

string = "Hello World"
new_string = string.replace("World", "world")
print(new_string)  

str = "Hello World"
if "Hello" in str:
    print("'Hello' found in the string.")
else:
    print("'Hello' not found in the string.")

str = "ho World"
if "Hello" not in str:
    print("'Hello' not found in the string.")
else:
    print("'Hello' found in the string.")
