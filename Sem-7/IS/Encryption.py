def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # check if the character is a letter
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char  # non-alphabet characters remain unchanged
    return encrypted_text

def encrypt_file(input_file, output_file, shift):
    try:
        # Read plaintext from input file
        with open(input_file, 'r') as file:
            plaintext = file.read()

        # Encrypt plaintext
        encrypted_text = caesar_cipher_encrypt(plaintext, shift)

        # Write encrypted text to output file
        with open(output_file, 'w') as file:
            file.write(encrypted_text)

        print(f"Encryption successful. Encrypted file saved as {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An IOError occurred during file processing.")

# Get user input for encryption key, input file, and output file
try:
    shift = int(input("Enter the encryption key (a number between 1 and 25): "))
    if not (1 <= shift <= 25):
        raise ValueError("Key must be between 1 and 25")

    input_file = input("Enter the path to the input file: ").strip()
    output_file = input("Enter the path to save the encrypted file: ").strip()

    encrypt_file(input_file, output_file, shift)

except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nEncryption process interrupted.")
