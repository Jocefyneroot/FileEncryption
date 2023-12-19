# Challenge: File Encryption
# Task: Try to create a decryption script and improve the encryption algorithm.

from itertools import cycle


def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            # Read the content of the file
            content = file.read()

        # Convert the key to bytes
        key_bytes = key.encode("utf-8")

        # Encrypt the content using XOR
        encrypted_content = bytes(
            [b ^ key_byte for b, key_byte in zip(content, cycle(key_bytes))]
        )

        # Write the encrypted content back to the file
        with open(file_path + ".encrypted", "wb") as encrypted_file:
            encrypted_file.write(encrypted_content)

        print(f"Encryption successful. Encrypted file saved as {file_path}.encrypted")

    except Exception as e:
        print(f"Error during encryption: {e}")


# Example
file_path = "sample.txt"
encryption_key = "my_secret_key"
encrypt_file(file_path, encryption_key)
