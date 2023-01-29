# class to store a data
class Data:
    def __init__(self):
        self.morse_code = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}


# main program

# getting the user input
def get_input():
    return input('Message to convert: ')


# encrypting the message
def encrypt(message):
    data = Data()
    return " ".join([data.morse_code[char] for char in list(message.upper())])


# decrypting the message
def decrypt(dec_message):
    data = Data()
    message = ''
    for char in dec_message.split(' '):
        for key, val in data.morse_code.items():
            if char == val:
                message += key
    return message.lower()


