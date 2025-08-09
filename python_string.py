print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#slicing 
Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
Use negative indexes to start the slice from the end of the string:
print(b[-5:-2])
The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))
Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#string fromatting
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)
text formatting is important
#python escape character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."
this above will giev u error
txt = "We are the so-called \"Vikings\" from the north."
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
