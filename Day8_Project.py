# Day 8 Project
# Ceaser Cipher

# Ceaser Cipher is an encoding and decoding game
# The goal is to encrypt (decrypt) a message using a positional shifts in the alphabet

# Rules for encoding:
# enter a string / phrase
# ask for a positional shift in the alphabet
# shift the alphabet 
# generate a new string based on original string /phrase
# output phrase

# decoded word should be the reverse of the encoded word


def encode_word(phrase, shift):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    encoded_alpha = alphabet[shift-1:] + alphabet[0:shift-1]    
    #print(encoded_alpha)
    text_position = []
   
    for letter in phrase:
        for index, item in enumerate(alphabet):
            if letter == item:
                text_position.append(index)
    #print(text_position)
    encoded_word =[]

    for index in text_position:
        encoded_word.append(encoded_alpha[index])

    #print(encoded_word)

    encoded = "".join(encoded_word)
    #print(encoded)
    return encoded

def decode_word(phrase, shift):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    encoded_alpha = alphabet[shift-1:] + alphabet[0:shift-1]
    #print(encoded_alpha)
    text_position = []
    # this is wrong
    for letter in phrase:
        for index, item in enumerate(encoded_alpha):
            if letter == item:
                text_position.append(index)
    #print(text_position)
    decoded_word =[]

    for index in text_position:
        decoded_word.append(alphabet[index])

    #print(decoded_word)

    decoded = "".join(decoded_word)
    #print(decoded)
    return decoded


encode_decode = input("Do you want to encode a word or decode:").lower()

if encode_decode == "encode":
    text_input = input("Please enter the text to be encoded: ").lower()
    shift_text = int(input("Please enter the positional shift: "))
    new_encode = encode_word(text_input, shift_text)
    print(f"The encoded word is {new_encode}")

else:
    text_input = input("Please enter the text to be decoded: ").lower()
    shift_text = int(input("Please enter the positional shift: "))
    new_decode = decode_word(text_input, shift_text)
    print(f"The decoded word is {new_decode}")


