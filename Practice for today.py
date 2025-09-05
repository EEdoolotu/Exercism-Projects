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
    
        
        
#sublist exercise
"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sublist(a, b):
    if not a:
        return True
    if len(a) > len(b):
        return False
    for i in range(len(b) - len(a) + 1):
        if b[i:i + len(a)] == a:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_two, list_one):
        return SUPERLIST
    if is_sublist(list_one, list_two):
        return SUBLIST

    return UNEQUAL
        
       
#fcc caesar cipher
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
#RPG Character
full_dot = '●'
empty_dot = '○'
max_dots = 10

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string" 
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    stats = {"strength":strength, "intelligence":intelligence, "charisma":charisma}

    for stat in stats.values():
        if not isinstance(stat, int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(stats.values()) != 7:
        return "The character should start with 7 points"

    return "\n".join([
        name,
        f"STR {full_dot * strength}{empty_dot * (max_dots - strength)}",
        f"INT {full_dot * intelligence}{empty_dot * (max_dots - intelligence)}",
        f"CHA {full_dot * charisma}{empty_dot * (max_dots - charisma)}",
    ])

#pin extractor
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
#pattern generator
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    return " ".join(str(i) for i in range(1, n +1))
#data validator
import re


medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):

    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }

    return [key for key, value in constraints.items() if not value]


def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            val = dictionary.get(key)
            print(f"Unexpected format '{key}: {val}' at position {index}.")
            is_invalid = True

    
    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)
#user config
test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}
def add_setting(settings: dict, new_pair: tuple) -> str:
    key, value = new_pair
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, new_pair: tuple) -> str:
    key, value = new_pair
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict, key: str) -> str:
    key = str(key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."   # ✅ must end with newline

    result = ["Current User Settings:"]
    for key, value in settings.items():
        result.append(f"{key.capitalize()}: {value}")
    return "\n".join(result) + "\n"          # ✅ must end with newline
#isbn
def validate_isbn(isbn, length):
    # Ensure the provided ISBN matches the specified length
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Separate main digits and check digit correctly (off-by-one fix)
    if length == 10:
        main_digits = isbn[:9]
        given_check_digit = isbn[9]
        # Validate characters: first 9 must be digits; check digit can be 0-9 or 'X'
        if not main_digits.isdigit() or not (given_check_digit.isdigit() or given_check_digit == 'X'):
            raise ValueError('Invalid character was found.')

        main_digits_list = [int(d) for d in main_digits]
        expected_check_digit = calculate_check_digit_10(main_digits_list)

    else:  # length == 13
        main_digits = isbn[:12]
        given_check_digit = isbn[12]
        # All 13 must be digits for ISBN-13
        if not (main_digits.isdigit() and given_check_digit.isdigit()):
            raise ValueError('Invalid character was found.')

        main_digits_list = [int(d) for d in main_digits]
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Check if the given check digit matches the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')

    # Handle missing comma / not comma-separated (IndexError)
    try:
        isbn = values[0]
        length_str = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return

    # Handle non-numeric length (ValueError)
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    # Only allow 10 or 13
    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    # Validate ISBN; handle invalid characters raised by validate_isbn
    try:
        validate_isbn(isbn, length)
    except ValueError:
        print('Invalid character was found.')


# main()  # <- Keep commented out for the tests to run properly.
