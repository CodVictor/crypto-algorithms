def xor_cipher(text, key):
    result = []

    for i, char in enumerate(text):
        x = ord(char) ^ ord(key[i % len(key)])
        result.append(chr(x))

    return "".join(result)

# Ejemplo de uso
cipher_text = "({!+8b*+"
key = "XOR"

decoded_text = xor_cipher(cipher_text, key)
print("Texto resultante:", decoded_text)