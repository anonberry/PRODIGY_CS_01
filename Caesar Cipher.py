def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep spaces, numbers and symbols unchanged
            result += char

    return result


print("===<<<<<<< Caesar Cipher >>>>>>>===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Enter E to encrypt or D to decrypt: ").upper()

if choice == "E":
    encrypted = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted)

elif choice == "D":
    decrypted = caesar_cipher(message, -shift)
    print("Decrypted message:", decrypted)

else:
    print("Invalid choice. Please enter E or D.")