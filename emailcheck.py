text=input("Please enter your email: ")

x=text.find("@")
y=text.find(".")

if "@" in text and text.count("@")==1 and "." in text and text.count(".")==1 and (y>x):
    print("Valid")
else:
    print("Invalid")