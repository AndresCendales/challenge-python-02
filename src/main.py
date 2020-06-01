# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Define el largo de la clave
    lenght = random.randint(8,16)
    
    #inicializamos la clave y variables para pre-validacion
    password = []
    has_low = False
    has_upper = False
    has_digit = False
    has_symbol = False
    
    #Loop que se repite a menos que la contrasena sea segura
    while True:
        for idx in range(lenght):
            type_char = random.randint(0,3)

            if type_char == 0:
                password.append(chr(random.randint(97,122)))
                has_low = True
            elif type_char ==  1:
                password.append(chr(random.randint(65,90)))
                has_upper = True
            elif type_char == 2:
                password.append(chr(random.randint(48,57)))
                has_digit = True
            elif type_char == 3:
                password.append(SYMBOLS[random.randint(0,len(SYMBOLS)-1)])
                has_symbol = True
        
        #Pre-validacion para asegurarse que contiene al menos un caracter de cada tipo (minuscula, mayuscula, digito y simbolo)
        if has_low == False or has_upper == False or has_digit == False or has_symbol == False:
            has_low = False
            has_upper = False
            has_digit = False
            has_symbol = False
            del password[:]
        else: 
            break  
        
    return ''.join(password)

def validate(password):
    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()

    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
