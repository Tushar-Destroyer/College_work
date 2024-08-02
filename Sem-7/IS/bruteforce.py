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

def brute_force_decrypt(input_file):
    try:
        # Read encrypted text from input file
        with open(input_file, 'r') as file:
            encrypted_text = file.read()

        # Initialize variables to store the best decrypted result and its corresponding key
        best_decryption = ""
        best_key = 0

        # Brute-force attack to decrypt using all possible keys (1 to 25)
        for shift in range(1, 26):
            decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
            print(f"Trying with key = {shift}: {decrypted_text[:100]}")  # Print first 100 characters of decrypted text

            # Evaluate the quality of the decryption (e.g., using frequency analysis or pattern matching)
            # For simplicity, here we compare the length of decrypted text (a naive measure)
            if len(decrypted_text) > len(best_decryption):
                best_decryption = decrypted_text
                best_key = shift

        # Print the best decryption result found
        print(f"\nBest decryption with key = {best_key}: {best_decryption}")

        # Optionally, write the best decryption result to an output file
        with open('decrypted_output.txt', 'w') as output_file:
            output_file.write(best_decryption)

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An IOError occurred during file processing.")

# Get user input for input file
try:
    input_file_path = input("Enter the path to the encrypted file: ").strip()

    brute_force_decrypt(input_file_path)

except KeyboardInterrupt:
    print("\nBrute-force attack interrupted.")
