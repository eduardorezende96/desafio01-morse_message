from collections import Counter
import dictionary
import re


def start(message):
    counter = Counter(message)
    is_morse = counter['.'] + counter['-'] + counter[' ']

    if is_morse == len(message):
        morse_to_txt(message)

    else:
        txt_to_morse(message)


def morse_to_txt(morse):
    morse_letter = re.split(r"\s", morse)
    trans_message = ''

    for k in range(len(morse_letter)):
        teste1 = dictionary.translate_morse(morse_letter[k])
        trans_message = trans_message + teste1

    print(" → translation: ", trans_message)


def txt_to_morse(txt):
    # print("not morse:", txt)
    trans_message = ''
    for i in range(len(txt)):
        letter = dictionary.translate_letter(txt[i])
        trans_message = trans_message + letter + ' '

    print(" → translation: ", trans_message)
