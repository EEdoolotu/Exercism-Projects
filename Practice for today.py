def square_root(number):
    if number <= 0:
        raise ValueError("Pls Enter a valid integer")
    for i in range(number + 1):
        if i * i == number:
            return i

    raise ValueError("Pls enter a valid whole number")



#leap year function
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


#Functions for Triangles
def equilateral(sides):
    a, b, c = sides
    return a == b == c and a > 0


def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or c == b) and a + b >= c and b + c >= a and a + c >= b


def scalene(sides):
    a, b, c = sides
    return a != b and a != c and b!=c and a + b >= c and b + c >= a and a + c >= b

#conditional exercise 1
def response(hey_bob):
    hey_bob = hey_bob.strip()

    if not hey_bob.strip():
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
        
    
