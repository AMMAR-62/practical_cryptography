# Partial listing: Some Assembly Required.
import string

def create_shift_substitution(n: int):
    encoding = {}
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter

    return encoding, decoding

def encode(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

# one-liner encod:
def encode_line(message, subst):
    return "".join(subst.get(x,x) for x in message)

def decode(message, subst):
    return encode(message, subst)

def printable_substitution(subst):
    # sort by source character so things are alphatbetized.
    mapping = sorted(subst.items())

    # Then create two lines: source above, target beneath.
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return f"{alphabet_line}\n{cipher_line}"


