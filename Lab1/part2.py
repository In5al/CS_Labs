def remove_whitespace(text):
    return "".join(text.split())

def generate_new_alphabet(key2):
    if not key2.isalpha() or len(key2) < 7:
        return None

    seen = set()
    new_alphabet = ""

    for char in key2:
        char = char.upper()
        if char.isalpha() and char not in seen:
            new_alphabet += char
            seen.add(char)

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            new_alphabet += char

    return new_alphabet

def cipher2(text, key1, key2, string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_alphabet = generate_new_alphabet(key2)

    if key1 < 0 or key1 > 25:
        print("The first key should be in range 0 - 25")
        return

    if not new_alphabet or len(new_alphabet) != 26:
        print("Key 2 should be a valid permutation of the alphabet with exactly 26 unique characters.")
        return

    print_new_alphabet(new_alphabet)
    result = ""

    for char in text:
        if char.isalpha():
            char = char.upper()
            if string == 'e':
                shifted_index = (new_alphabet.index(char) + key1) % 26
            elif string == 'd':
                shifted_index = (new_alphabet.index(char) - key1) % 26

            shifted_char = new_alphabet[shifted_index]
            if char.islower():
                shifted_char = shifted_char.lower()
            result += shifted_char
        else:
            result += char

    print(result)

def print_new_alphabet(new_alphabet):
    print(f"Advanced alphabet: {new_alphabet}")

text = input('Enter your text: ').upper()
text = remove_whitespace(text)
key1 = int(input('Enter the first key (0 - 25): '))
key2 = input('Enter key 2 (a string of letters with at least 7 characters): ').upper()
string = input('Choose "e" for encryption or "d" for decryption: ')

cipher2(text, key1, key2, string)
