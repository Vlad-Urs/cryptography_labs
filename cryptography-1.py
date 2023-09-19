

def print_menu():
    print('encrypt one key:   1')
    print('encrypt two keys:  2')
    print('decrypt one key:   3')
    print('decrypt two keys:  4')
    print('close:             5+')

def encrypt(text, seq, key):
    res = ''

    for i in range(len(text)):
        char = text[i]

        pos = (seq.rfind(char) + key - 26) % 26
        res += seq[pos]

    return res

def get_key():
    key = 0

    # get the key
    while True:
        try:
            key = int(input('input integer key: '))
        except ValueError:
            print('enter a valid number for key')
            continue
        if key < 1 or key > 25:
            print('enter a valid number for key')
            continue
        else:
            break

    return key

def get_message():
    m = ''

    while True:
        m = input('input the message: ')
        m = m.replace(" ", "")
        m = m.upper()
        bad = False
        for char in m:
            if not char.isalpha():
                bad = True
                break
        if bad:
            print('enter a valid message')
            continue
        else:
            break

    return m

def get_text_key():
    m = ''

    while True:
        m = input('input the text key: ')
        m = m.upper()
        bad = False
        for char in m:
            if not char.isalpha():
                bad = True
                break
        if bad:
            print('enter a valid key')
            continue
        else:
            break

    return m


def permutate(word, alphabet):
    new_alpha = ''

    for char in word:
        if char not in new_alpha:
            new_alpha += char
            alphabet = alphabet.replace(char, '')

    new_alpha += alphabet

    return new_alpha

if __name__ == "__main__":
    while True:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print_menu()

        x = 0

        while True:
            try:
                x = int(input('number: '))
            except ValueError:
                print('enter a valid number')
                continue
            else:
                break

        if x >= 5:
            break

        # encrypt one key
        if x == 1:
            encryption_key = get_key()
            message = get_message()
            print('encrypted message: ', end = '')
            print(encrypt(message, alphabet, encryption_key) + "\n")
            continue

        # encrypt two keys
        if x == 2:
            integer_key = get_key()
            text_key = get_text_key()
            new_alpha = permutate(text_key, alphabet)
            print(f'new alphabet: {new_alpha}')
            message = get_message()
            print('encrypted message: ', end='')
            print(encrypt(message, new_alpha, integer_key) + "\n")
            continue

        # decrypt one key
        if x == 3:
            decryption_key = get_key()
            message = get_message()
            print('encrypted message: ', end='')
            print(encrypt(message, alphabet, decryption_key*(-1)) + "\n")
            continue

        # decrypt two keys
        if x == 4:
            integer_key = get_key()
            text_key = get_text_key()
            new_alpha = permutate(text_key, alphabet)
            print(f'new alphabet: {new_alpha}')
            message = get_message()
            print('encrypted message: ', end='')
            print(encrypt(message, new_alpha, integer_key*(-1)) + "\n")
            continue
