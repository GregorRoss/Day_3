def return_10():
    return 10

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string1):
    return len(string1)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(Month):
    if Month == 1:
        return "January"
    elif Month == 2:
        return "Febraury"
    elif Month == 3:
        return "March"
    elif Month == 4:
        return "April"
    elif Month == 5:
        return "May"
    elif Month == 6:
        return "June"
    elif Month == 7:
        return "July"
    elif Month == 8:
        return "August"
    elif Month == 9:
        return "September"
    elif Month == 10:
        return "October"
    elif Month == 11:
        return "November"
    elif Month == 12:
        return "December"
    

def number_to_short_month_name(Month):
        if Month == 1:
            return "Jan"
        elif Month == 2:
            return "Feb"
        elif Month == 3:
            return "Mar"
        elif Month == 4:
            return "Apr"
        elif Month == 5:
            return "May"
        elif Month == 6:
            return "Jun"
        elif Month == 7:
            return "Jul"
        elif Month == 8:
            return "Aug"
        elif Month == 9:
            return "Sep"
        elif Month == 10:
            return "Oct"
        elif Month == 11:
            return "Nov"
        elif Month == 12:
            return "Dec"
        
def volume_of_cube(length):
    return length * length * length

def reverse_string(String):
    str =""
    for i in String:
        str = i + str
    return str

def fahrenheit_to_celsius(temp_f):
    return (temp_f -32) * 5/9

 