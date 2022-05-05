def translate_letter(letter):
    if letter == ' ':
        return ''

    elif letter == 'a' or letter == 'A':
        return '.-'

    elif letter == 'b' or letter == 'B':
        return '-...'

    elif letter == 'c' or letter == 'C':
        return '-.-.'

    elif letter == 'd' or letter == 'D':
        return '-..'

    elif letter == 'e' or letter == 'E':
        return '.'

    elif letter == 'f' or letter == 'F':
        return '..-.'

    elif letter == 'g' or letter == 'G':
        return '--.'

    elif letter == 'h' or letter == 'H':
        return '....'

    elif letter == 'i' or letter == 'I':
        return '..'

    elif letter == 'j' or letter == 'J':
        return '.---'

    elif letter == 'k' or letter == 'K':
        return '-.-'

    elif letter == 'l' or letter == 'L':
        return '.-..'

    elif letter == 'm' or letter == 'M':
        return '--'

    elif letter == 'n' or letter == 'N':
        return '-.'

    elif letter == 'o' or letter == 'O':
        return '---'

    elif letter == 'p' or letter == 'P':
        return '.--.'

    elif letter == 'q' or letter == 'Q':
        return '--.-'

    elif letter == 'r' or letter == 'R':
        return '.-.'

    elif letter == 's' or letter == 'S':
        return '...'

    elif letter == 't' or letter == 'T':
        return '-'

    elif letter == 'u' or letter == 'U':
        return '..-'

    elif letter == 'v' or letter == 'V':
        return '...-'

    elif letter == 'w' or letter == 'W':
        return '.--'

    elif letter == 'x' or letter == 'X':
        return '-..-'

    elif letter == 'y' or letter == 'Y':
        return '-.--'

    elif letter == 'z' or letter == 'Z':
        return '--..'

    elif letter == '1':
        return '.----'

    elif letter == '2':
        return '..---'

    elif letter == '3':
        return '...--'

    elif letter == '4':
        return '....-'

    elif letter == '5':
        return '.....'

    elif letter == '6':
        return '-....'

    elif letter == '7':
        return '--...'

    elif letter == '8':
        return '---..'

    elif letter == '9':
        return '----.'

    elif letter == '0':
        return '-----'


def translate_morse(letter):
    if letter == ' ':
        return ''

    elif letter == '.-':
        return 'a'

    elif letter == '-...':
        return 'b'

    elif letter == '-.-.':
        return 'c'

    elif letter == '-..':
        return 'd'

    elif letter == '.':
        return 'e'

    elif letter == '..-.':
        return 'f'

    elif letter == '--.':
        return 'g'

    elif letter == '....':
        return 'h'

    elif letter == '..':
        return 'i'

    elif letter == '.---':
        return 'j'

    elif letter == '-.-':
        return 'k'

    elif letter == '.-..':
        return 'l'

    elif letter == '--':
        return 'm'

    elif letter == '-.':
        return 'n'

    elif letter == '---':
        return 'o'

    elif letter == '.--.':
        return 'p'

    elif letter == '--.-':
        return 'q'

    elif letter == '.-.':
        return 'r'

    elif letter == '...':
        return 's'

    elif letter == '-':
        return 't'

    elif letter == '..-':
        return 'u'

    elif letter == '...-':
        return 'v'

    elif letter == '.--':
        return 'w'

    elif letter == '-..-':
        return 'x'

    elif letter == '-.--':
        return 'y'

    elif letter == '--..':
        return 'z'

    elif letter == '.----':
        return '1'

    elif letter == '..---':
        return '2'

    elif letter == '...--':
        return '3'

    elif letter == '....-':
        return '4'

    elif letter == '.....':
        return '5'

    elif letter == '-....':
        return '6'

    elif letter == '--...':
        return '7'

    elif letter == '---..':
        return '8'

    elif letter == '----.':
        return '9'

    elif letter == '-----':
        return '0'

    elif letter == '':
        return ' '
