def remove_whitespace(text):
    return "".join(text.split())

def encrypt(text, key):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        else:
            print("The text should be in range A - Z or a - z")
            return None
    return result

def decrypt(text, key):
    return encrypt(text, -key)

def main():
    text = input('Enter your text: ').upper()
    text = remove_whitespace(text)
    key = int(input('Enter the key (0 - 25): '))

    if key < 0 or key > 25:
        print('The key should be in range 0 - 25')
        return

    operation = input('Choose "e" for encryption or "d" for decryption: ')

    if operation == 'e':
        result = encrypt(text, key)
        if result:
            print(result)
    elif operation == 'd':
        result = decrypt(text, key)
        if result:
            print(result)
    else:
        print('Invalid operation. Please choose "e" or "d".')

if __name__ == "__main__":
    main()
