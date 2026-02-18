alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]

def encrypt(original_text, shift_amount):
    cipher_text = ''
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            if shifted_position > len(alphabet):
                shifted_position -= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f'This is the encoding text: {cipher_text}')

def decrypt(encrypted_text, unshift_amount):
    uncipher_text = ''
    for letter in encrypted_text:
        if letter not in alphabet:
            uncipher_text += letter
        else:
            shifted_position = alphabet.index(letter) - unshift_amount
            if shifted_position < 0:
                shifted_position += len(alphabet)
            uncipher_text += alphabet[shifted_position]
    print(f'This is the decoding text: {uncipher_text}')

direction = input('Type "encode" to encrypt, type "decode" to decrypt: ').lower()
if direction == 'encode':
    text = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))
    encrypt(text, shift)
elif direction == 'decode':
    text = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))
    decrypt(text, shift)
else:
    print('Wrong entrey!')
