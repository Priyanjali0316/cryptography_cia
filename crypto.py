# Caesar Cipher using Polynomial Hash

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


# 🔁 Test Function
def run_test(text, key):
    print("\n--- Test Case ---")
    print("Plaintext:", text)
    print("Key:", key)

    # Step 1: Hash
    hash_value = get_hash(key)

    # Step 2: Shift
    shift = hash_value % 26

    print("Hash Value:", hash_value)
    print("Shift:", shift)

    # Step 3: Encryption
    encrypted = encrypt(text, shift)
    print("Encrypted:", encrypted)

    # Step 4: Decryption
    decrypted = decrypt(encrypted, shift)
    print("Decrypted:", decrypted)

    # Step 5: Verification
    if decrypted == text:
        print("✔ Round-trip successful")
    else:
        print("❌ Error")



if __name__ == "__main__":

    print("=== Caesar Cipher using Hashing ===")

    text = input("Enter text: ").strip()
    key = input("Enter key: ").strip()

    run_test(text, key)

    print("\n=== Additional Test Cases ===")
    run_test("hello", "abc")   
    run_test("world", "data")  