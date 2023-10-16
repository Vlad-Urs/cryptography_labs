def print_menu():
    print('encrypt: 1')
    print('decrypt: 2')
    print('close: 3')


def validate_key(key):
    if len(key) < 7 or not key.isalpha():
        return False
    return True

def build_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZȘȚĂÂÎ"
    key = key.upper()
    new_alpha = ''
    matrix = [[0 for _ in range(5)] for _ in range(6)]

    for char in key:
        if char not in new_alpha:
            new_alpha += char
            alphabet = alphabet.replace(char, '')

    new_alpha += alphabet
    index = 0


    for i in range(6):
        for j in range(5):
            matrix[i][j] = new_alpha[index]
            index += 1
            print(f'{matrix[i][j]} ', end = '')
        print()


    return matrix

def find_position(matrix, char):
    for i in range(6):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair(plaintext, matrix, operation):
    if len(plaintext) % 2 != 0:
        plaintext += 'V'
        
    text = ""

    for i in range(0, len(plaintext) - 1, 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            col1 = (col1 + operation) % 5
            col2 = (col2 + operation) % 5
        elif col1 == col2:
            row1 = (row1 + operation) % 5
            row2 = (row2 + operation) % 5
        else:
            col1, col2 = col2, col1

        text += matrix[row1][col1] + matrix[row2][col2]

    return text



if __name__ == "__main__":
    while True:
        print_menu()
        choice = input('Select an option: ')

        if choice == '1':
            key = input('Enter the key (at least 7 letters, only letters): ')
            key = key.replace(' ', '').upper()
            key = key.replace('J', 'I')
            if not validate_key(key):
                print('Invalid key. Please follow the key requirements.')
                continue
            matrix = build_playfair_matrix(key)
            plaintext = input('Enter the plaintext (letters only): ')
            plaintext = plaintext.replace(' ', '').upper()
            plaintext = plaintext.replace('J', 'I')
            if not plaintext.isalpha():
                print('enter a valid text')
                continue
            ciphertext = playfair(plaintext, matrix, 1)
            print('Encrypted message:', ciphertext)



        elif choice == '2':
            key = input('Enter the key (at least 7 letters, only letters): ')
            key = key.replace(' ', '').upper()
            key = key.replace('J', 'I')
            if not validate_key(key):
                print('Invalid key. Please follow the key requirements.')
                continue
            matrix = build_playfair_matrix(key)
            ciphertext = input('Enter the ciphertext (letters only): ')
            ciphertext = ciphertext.replace(' ', '').upper()
            ciphertext = ciphertext.replace('J', 'I')
            if not ciphertext.isalpha():
                print('enter a valid text')
                continue
            plaintext = playfair(ciphertext, matrix, -1)
            print('Decrypted message:', plaintext)
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please select a valid option.')