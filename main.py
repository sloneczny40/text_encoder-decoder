alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


def encrypt(text, shift):
    encrypted_text = ""
    list_of_words = list(text)
    for i in list_of_words:
        if i in alphabet:
            index_of_letter = alphabet.index(i) + shift
            if index_of_letter > 25:
                index_of_letter -= 26
            new_letter = alphabet[index_of_letter]
            encrypted_text += new_letter
        else:
            encrypted_text += i
    print(index_of_letter)
    print(f"The encoded text is: {encrypted_text}")





if direction == 'encode':
    encrypt(text, shift)
# elif direction == 'decode':
    # decode(text, shift)
# else:
#     print("You need to type 'encode' or 'decode'\n")
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
