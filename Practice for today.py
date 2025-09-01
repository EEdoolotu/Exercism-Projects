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
        
    
#contionals 2 
def convert(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result if result else str(number)


#Pig Latin
def translate(text):
    def translate_word(word: str) -> str:
        vowels = "aeiou"
        w = word

        # Rule 1: starts with vowel OR "xr"/"yt"
        if w[0].lower() in vowels or w.startswith(("xr", "yt")):
            return w + "ay"

        # Rule 3 (special case): leading "qu"
        if w[:2].lower() == "qu":
            return w[2:] + "quay"

        # Rules 2 & 3: move consonant cluster (bundle any trailing 'qu')
        for i, ch in enumerate(w):
            if ch.lower() in vowels:
                # If this vowel is 'u' and immediately preceded by 'q', treat 'qu' as consonant cluster
                if i > 0 and w[i-1:i+1].lower() == "qu":
                    i += 1  # include the 'u'
                return w[i:] + w[:i] + "ay"

        # Rule 4: treat 'y' as a vowel if we saw no a/e/i/o/u
        if "y" in w:
            j = w.lower().index("y")
            return w[j:] + w[:j] + "ay"

        # Fallback (rare: no vowels at all and no 'y')
        return w + "ay"

    return " ".join(translate_word(w) for w in text.split())

#matching brackets
def is_paired(input_string):
    openers = {"(", "{" , "["}
    matches = {")":"(", "]":"[", "}":"{"}
    stack = []

    for ch in input_string:
        if ch in openers:
            stack.append(ch)
        elif ch in matches:
            if not stack or stack[-1] != matches[ch]:
                return False

            stack.pop()
    return not stack