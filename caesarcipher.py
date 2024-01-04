# The English alphabet
letters = "abcdefghijklmnopqrstuvwxyz"

# The number of letters in the alphabet
num_letters = len(letters)

# This function uses the Caesar cipher to encrypt sentence.
def encrypt_mode(sentence, key):
    chipher = ""
    for letter in sentence:
        letter = letter.lower()

        if not letter == " ":
            index = letters.find(letter)

            # If the letter is not in the alphabet, it's added directly.
            if index == -1:
                chipher += letter
                
            # Calculate new index after applying the key and adjust for rotation.
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                
                # Append the encrypted letter to the result.
                chipher += letters[new_index]
    return chipher

# This function uses the sentence to decrypt Caesar cipher.
def decrypt_mode(chipher, key):
    sentence = ""
    for letter in chipher:
        letter = letter.lower()

        if not letter == " ":
            index = letters.find(letter)

            # If the letter is not in the alphabet, it's added directly.
            if index == -1:
                sentence += letter

            # Calculate new index by reversing the key and adjust for rotation.
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                
                # Append the decrypted letter to the result.
                sentence += letters[new_index]
    return sentence

# This function can encrypt or decrypt text based on the mode.
def encrypt_decrypt_mode(text, mode, key):
    result = ""

    # If decryption is chosen, invert the key.
    if mode == "d":
        key = -key

    # Keep spaces as they are.
    for letter in text:
        if letter == " ":
            result += letter
            continue

        letter = letter.lower()
        index = letters.find(letter)

        # If the letter is not in the alphabet, it's added directly.
        if index == -1:
            result += letter

        # Calculate new index and adjust for rotation.
        else:
            new_index = index + key

            if new_index >= num_letters:
                new_index -= num_letters

            elif new_index < 0:
                new_index += num_letters

            # Append the result.
            result += letters[new_index]

    return result
            

# Main interface for the user to choose between encryption and decryption.
print("\n !!! CAESAR CHIPER PROGRAM !!! \n")

user_input = input("Do you want to (e)ncrypt or (d)ecrypt? (e/d): ").lower()
print()

if user_input == "e":
    print("Encryption mode selection.")
    print()

    # User inputs for the key and the message.
    key = int(input("Please enter the key (0 to 25) to use. \n"))
    text = input("Enter the message to encrypt. \n")

    # Perform encryption.
    chipher = encrypt_decrypt_mode(text, user_input, key)
    print(f"Chipher text is: {chipher.upper()}")
    print("Full encrypted text copied to clipboard.")

elif user_input == "d":
    print("Decryption mode selection.")
    print()

    # User inputs for the key and the message.
    key = int(input("Please enter the key (0 to 25) to use. \n"))
    text = input("Enter the message to decrypt. \n")

    # Perform decryption.
    sentence = encrypt_decrypt_mode(text, user_input, key)
    print(f"Plain text is: {sentence.upper()}")
    print("Full decrypted text copied to clipboard.")