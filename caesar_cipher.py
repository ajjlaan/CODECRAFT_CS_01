def caesar_cipher(message, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in message:
        if char.isalpha():
            ascii = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii + shift) % 26
            result += chr(ascii + shifted)
        else:
            result += char

    return result


def main():
    print("Caesar Cipher Tool")
    print("----------------------")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Choose an option (1/2): ")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == "1":
        enc = caesar_cipher(message, shift, "encrypt")
        print("\nEncrypted Message:", enc)

    elif choice == "2":
        dec = caesar_cipher(message, shift, "decrypt")
        print("\nDecrypted Message:", dec)

    else:
        print("Invalid choice!")



main()