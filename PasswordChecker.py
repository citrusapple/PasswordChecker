import string
alpha = string.ascii_lowercase
ALPHA = string.ascii_uppercase
numbers = string.digits

def checkio(password):
    lower_case = False;
    upper_case = False;
    num = False;
    if len(password) < 10:
        print("size does matter, let's make this more than 10 characters yea?");
        return False;
    else:
        for char in password:
            if char in alpha:
                lower_case = True;
            if char in ALPHA:
                upper_case = True;
            if char in numbers:
                num = True;
    if lower_case and upper_case and num == True:
        print("Keep those secrets locked away! Awesome password!")
        return True;
    else:
        if lower_case == False:
            print("gimme some lowercases!");
            return False;
        if upper_case == False:
            print("gimme some uppercases!");
            return False;
        if num == False:
            print("gimme some digits! (and call me maybe)");
            return False;

print(checkio("adaDV121345"));