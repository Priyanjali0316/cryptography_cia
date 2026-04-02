from crypto import process

def run_test(text, key):
    print("\n--- Test Case ---")
    print("Plaintext:", text)
    print("Key:", key)

    hash_value, shift, encrypted, decrypted = process(text, key)

    print("Hash Value:", hash_value)
    print("Shift:", shift)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

    if decrypted == text:
        print("✔ Round-trip successful")
    else:
        print("❌ Error")


# 🔥 Two required test cases
print("=== Testing Caesar Cipher with Hashing ===")

run_test("hello", "abc")   # Example 1
run_test("world", "data")  # Example 2