"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
""""
def NoVowels(AnyString):
    vowels = ('a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O',
    'U')
    newString = ""
    for ch in AnyString:
        if ord(ch) is 97 or ord(ch) is 65:
            newString = newString + ""
        elif ord(ch) is 101 or ord(ch) is 69:
            newString = newString + ""
        elif ord(ch) is 105 or ord(ch) is 73:
            newString = newString + ""
        elif ord(ch) is 111 or ord(ch) is 79:
            newString = newString + ""
        elif ord(ch) is 117 or ord(ch) is 85:
            newString = newString + ""


        else:
            newString = newString + ch
        return newString
String = """Computer Science Makes the World go round but it doesn't make the world round itself!"""

code = final(NoVowels)
print(code)
"""Write an encryption code that you make up and run it for the variable NoVowels"""
def NoVowels(AnyString):
    vowels = ('a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O',
    'U')
    newString = ""
    for ch in AnyString:
        if ord(ch) is 97 or ord(ch) is 65:
            newString = newString + ":]"
        elif ord(ch) is 101 or ord(ch) is 69:
            newString = newString + "%"
        elif ord(ch) is 105 or ord(ch) is 73:
            newString = newString + "$"
        elif ord(ch) is 111 or ord(ch) is 79:
            newString = newString + "@"
        elif ord(ch) is 117 or ord(ch) is 85:
            newString = newString + "!"


        else:
            newString = newString + ch
        return newString
String = """Logan just made a new string of code"""

code = final(NoVowels)
print(code)
