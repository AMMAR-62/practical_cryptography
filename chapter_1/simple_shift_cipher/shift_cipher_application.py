#Partial Listing: Some assembly required:
from time import sleep
import creating_substitution_tables as cst
from termcolor import colored

if __name__ == "__main__":
    n = 1
    encoding, decoding = cst.create_shift_substitution(n)
    while True:
        print("\nShift Encoder Decoder")
        print("-----------------------")
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message")
        print("\t3. Decode Message")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()

        if(choice == '1'):
            print("Encoding Table:")
            print(cst.printable_substitution(encoding))
            print("Decoding Table:")
            print(cst.printable_substitution(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print(f"Encoded Message: {cst.encode(message.upper(), encoding)}")
        
        elif choice == '3':
            message = input("\nMessage to decode: ")
            print(f"Decoded Message: {cst.decode(message.upper(), decoding)}")
        
        elif choice == '4':
            new_shift = input(f"\nNew Shift (currrently {n}): ")
            try:
                new_shift = int(new_shift)
                if(new_shift < 1):
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print(f"Shift {new_shift} is not a valid number")
            else:
                n = new_shift
                encoding, decoding = cst.create_shift_substitution(n)
        elif choice == '5':
            print("Terminating ... ")
            iteration = 3
            while(iteration>=0):
                print(f"This program will self destruct in {colored(iteration, 'red')} seconds", end="\r")
                iteration-=1
                sleep(1)
            print("thanks for using my substitution cipher algorithm\n")
            exit(0)
        else:
            print(f"Unkown option {choice}")
        
                

