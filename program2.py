# Print even length words in a string. 

# Sample String : ''I love coding" 

# Expected Result : “love, coding”

string=input("enter the string :")
word=string.split(" ")
for w in word:
    l=len(w)
    if(l%2==0):
        print(w,end=",")