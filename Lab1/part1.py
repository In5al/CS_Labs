def remove(text):
    return "".join(text.split())

def cipher(text, key, string):
        if key > 25 or key < 0 :
            print('The key should be in range 0 - 25')
        else:
            for char in text:
                if not ('A' <= char <= 'Z'):
                    print("The text should be in range A - Z or a - z")
                    return
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            if string == 'e':
                for i in range(len(text)):
                    char = text[i]
                    result += alphabet[(alphabet.index(char) + key) % 26]

            elif string == 'd':
                key = -key
                for i in range(len(text)):
                    char = text[i]
                    result += alphabet[(alphabet.index(char) + key) % 26]
            print(result)

text = input('Enter your text ').upper()
text = remove(text)
key = int(input('Enter the key '))
string = input('Choose e for encryption or d for decription ')
cipher(text, key, string)