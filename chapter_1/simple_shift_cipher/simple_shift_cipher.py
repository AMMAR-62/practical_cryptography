
def simple_shift_cipher(s, sentence):
    words = sentence.split(' ')
    i = 0
    for text in words:
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        words[i] = result
        i+=1
    sentence = ' '.join(words)
    return sentence


if __name__ == '__main__':
    shift = int(input("Enter the shift: "))
    sentence = input("Enter the sentence: ")
    sentence = simple_shift_cipher(s=shift, sentence=sentence)
    print(f"ciphered: {sentence}\n")
