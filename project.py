# Caesar Cipher Encryption and Decryption

# Function to encrypt the message
def encrypt_message(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            # Shift character within the alphabet (wrap around with modulo)
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt the message
def decrypt_message(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Reverse the shift
            offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - offset) % 26 + offset)
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char
    return decrypted_text

# Example usage
if _name_ == "_main_":
    while True:
        print("\nCaesar Cipher Tool")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypted_message = encrypt_message(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == "2":
            encrypted_message = input("Enter the encrypted message: ")
            shift = int(input("Enter the shift value (1-25): "))
            decrypted_message = decrypt_message(encrypted_message, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == "3":
            print("Exiting the tool.")
            break

        else:
            print("Invalid choice. Please try again.")
