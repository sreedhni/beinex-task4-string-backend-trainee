# Write a Python code to remove all characters except a            

# Sample String : 'exercises' 

# Expected Result : 'eee' (Removed all characters except special character : e) 
def remove_characters(string, character):
    return ''.join(char for char in string if char == character)

string = input("enter the string; ")
character_need = input("enter the letter; ")

result = remove_characters(string, character_need)
print(result)


