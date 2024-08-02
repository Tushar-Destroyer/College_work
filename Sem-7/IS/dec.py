def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # check if the character is a letter
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char  # non-alphabet characters remain unchanged
    return decrypted_text

def decrypt_file(input_file, output_file, shift):
    try:
        # Read encrypted text from input file
        with open(input_file, 'r') as file:
            encrypted_text = file.read()

        # Decrypt encrypted text
        decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

        # Write decrypted text to output file
        with open(output_file, 'w') as file:
            file.write(decrypted_text)

        print(f"Decryption successful. Decrypted file saved as {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An IOError occurred during file processing.")

# Get user input for decryption key, input file, and output file
try:
    shift = int(input("Enter the decryption key (a number between 1 and 25): "))
    if not (1 <= shift <= 25):
        raise ValueError("Key must be between 1 and 25")

    input_file = input("Enter the path to the input file (encrypted file): ").strip()
    output_file = input("Enter the path to save the decrypted file: ").strip()

    decrypt_file(input_file, output_file, shift)

except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nDecryption process interrupted.")
