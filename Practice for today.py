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

#panagram
def is_pangram(sentence):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']
    sentence = sentence.lower()
    for ch in alphabets:
        if ch not in sentence:
            return False
    return True

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
#Isogram
def is_isogram(string):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    string = string.lower()
    letters = [ch for ch in string if ch in alphabets]
    return len(set(letters)) == len(letters)
            
        
#isbn task
def is_valid(isbn):
    s = isbn.replace("-", "").replace(" ","")
    if len(s) != 10:
        return False
    if not s[:9].isdigit():
        return False
    if not (s[9].isdigit() or s[9] == "X"):
        return False

    digits = [int(ch) for ch in s[:9]]
    check = 10 if s[9] == "X" else int(s[9])
    digits.append(check)
    total = sum((10 - i) * digits[i] for i in range(10))
    return total % 11 == 0

#caesar shift
def rotate(text, key):
    result =""
    for ch in text:
        if ch.isupper():
            result+= chr((ord(ch) - 65 + key) % 26 + 65 )
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    return result 
    
#darts 
def score(x, y):
    distance = (x **2 + y **2) ** 0.5

    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else: 
        return 0
#perfect number
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    total = sum(i for i in range(1, number) if number % i == 0)
        
    if total == number:
        return "perfect"
    elif number < total:
        return "abundant"
    else:
        return "deficient"
    
        
        
