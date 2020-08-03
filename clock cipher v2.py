Cipher = {
    'single_character': {
        ':': '',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h',
        '8': 'i',
        '9': 'j'
    },
    'double_character' : {
        '00': ' ',
        'AM': 'a',
        '10': 'k',
        '11': 'l',
        '12': 'm',
        '13': 'n',
        '14': 'o',
        '15': 'p',
        '16': 'q',
        '17': 'r',
        '18': 's',
        '19': 't',
        '20': 'u',
        '21': 'v',
        '22': 'w',
        '23': 'x',
        '24': 'y',
        'PM': 'z'
    }

}



def decrypt_text(text):

    for cipher in Cipher['double_character'].keys():
        if cipher in text.lower():
            text = text.replace(cipher, Cipher['double_character'][cipher])

    for cipher in Cipher['single_character'].keys():
        if cipher in text.lower():
            text = text.replace(cipher, Cipher['single_character'][cipher])
        
    return text

def encrypt_text(text):

    def get_key(VALUE):

        for key, value in Cipher['single_character'].items():
            if value == VALUE:
                return key

        for key, value in Cipher['double_character'].items():
            if value == VALUE:
                return key

    for cipher in Cipher['single_character'].values():
        if cipher in text.lower():
            text = text.replace(cipher, get_key(cipher))
            
    for cipher in Cipher['double_character'].values():
        if cipher in text.lower():
            text = text.replace(cipher, get_key(cipher))
    
    n = len(text) - 1
    text = text[1:n]

    return text

running = True
while running:
    print()
    print("Clock Cipher")
    print("What do you want to do?")
    print("1: Encrypt")
    print("2: Decode")
    print("3: Exit")
    des = int(input("Decision: ")) 
    
    if des == 1:
        text =  str(input("Enter the text you want to encrypt: "))
        print(encrypt_text(text))

    elif des == 2:
        text =  str(input("Enter the text you want to decrypt: "))
        print(decrypt_text(text))

    elif des == 3:
        running = False
