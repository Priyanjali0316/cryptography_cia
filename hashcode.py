# Hash Function
def get_hash(key):
    p = 31
    m = 10**9 + 7
    hash_value = 0

    for ch in key:
        hash_value = (hash_value * p + ord(ch)) % m

    return hash_value


# Encryption
def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch
    return result


# Decryption
def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) - ord('a') - shift + 26) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            result += ch
    return result


# Main
text = input("Enter text: ")
key = input("Enter key: ")

hash_value = get_hash(key)
shift = hash_value % 26

print("Hash Value:", hash_value)
print("Shift:", shift)

encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)