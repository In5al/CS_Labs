def create_playfair_matrix(key):
    # Initialize a 5x6 matrix to store the Playfair key matrix
    matrix = [['' for _ in range(6)] for _ in range(5)]

    # Convert the key to uppercase and replace 'J' with 'I'
    key = key.upper().replace('J', 'I')

    # Create a string containing all unique characters in the key
    key_chars = ''.join(dict.fromkeys(key))

    # Fill the matrix with unique key characters
    i, j = 0, 0
    for char in key_chars:
        matrix[i][j] = char
        j += 1
        if j == 6:
            j = 0
            i += 1

    # Fill the remaining matrix cells with the remaining characters of the Romanian alphabet
    alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
    for char in alphabet:
        if char not in key_chars and char != 'J':
            matrix[i][j] = char
            j += 1
            if j == 6:
                j = 0
                i += 1

    return matrix


def preprocess_text(text):
    # Remove spaces and convert text to uppercase
    text = text.replace(' ', '').upper()
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    return text

def is_valid_character(char, matrix):
    # Check if a character is a valid Playfair character
    return char in ''.join(''.join(row) for row in matrix)

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = preprocess_text(plaintext)

    # Pad the plaintext with 'X' if its length is odd
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    encrypted_text = ''
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]

        row1, col1, row2, col2 = None, None, None, None
        for r, row in enumerate(matrix):
            if pair[0] in row:
                row1, col1 = r, row.index(pair[0])
            if pair[1] in row:
                row2, col2 = r, row.index(pair[1])

        if row1 is not None and row2 is not None and col1 is not None and col2 is not None:
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    ciphertext = preprocess_text(ciphertext)

    decrypted_text = ''
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]

        row1, col1, row2, col2 = None, None, None, None
        for r, row in enumerate(matrix):
            if pair[0] in row:
                row1, col1 = r, row.index(pair[0])
            if pair[1] in row:
                row2, col2 = r, row.index(pair[1])

        if row1 is not None and row2 is not None and col1 is not None and col2 is not None:
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return decrypted_text

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def generate_and_display_matrix(key):
    matrix = create_playfair_matrix(key)
    print("\nPlayfair Matrix:")
    display_matrix(matrix)

def main():
    key = input("Enter the key (in lowercase): ")
    generate_and_display_matrix(key)

    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            plaintext = preprocess_text(plaintext)
            if not all(is_valid_character(char, create_playfair_matrix(key)) for char in plaintext):
                print("Invalid characters in the plaintext.")
            else:
                encrypted_text = playfair_encrypt(plaintext, key)
                print("Encrypted text:", encrypted_text)
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            decrypted_text = playfair_decrypt(ciphertext, key)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
