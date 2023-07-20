  # Python-Decrypt
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Contoh penggunaan
plaintext = input("Masukkan Text Yang Mau Di Dekripsi: ")
shift = 5

# Dekripsi
decrypted_text = decrypt(plaintext, shift)
print("Teks terdekripsi:", decrypted_text)
