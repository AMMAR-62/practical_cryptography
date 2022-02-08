from simple_shift_cipher import creating_substitution_tables as cst
import enchant

d = enchant.Dict('en_US')
def automated_decoding(message: str):
    for i in range(26):
        list_of_words = message.split(" ")
        list_of_words = [cst.decode(word, i) for word in list_of_words]
        count = 0
        for i in list_of_words:
            if(d.check(i)):
                count += 1
        if count>(len(list_of_words)/2):
            return "".join(list_of_words)
            
    else:
        return "no relevant decode exists"

if __name__ == "__main__":
    string_message = input("enter a string to decode\n")
    print(automated_decoding(string_message))

