ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LEN = len(ALPHABET)
def vigenere_cipher(text, key, mode="encode"):
    result = []
    key_index = 0

    for char in text:
        if char in ALPHABET:
            text_pos = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_pos = ALPHABET.index(key_char)

            if mode == "encode":
                new_pos = (text_pos + key_pos) % ALPHABET_LEN
            elif mode == "decode":
                new_pos = (text_pos - key_pos) % ALPHABET_LEN
            else:
                raise ValueError("mode debe ser 'encode' o 'decode'")

            result.append(ALPHABET[new_pos])
            key_index += 1
        else:
            result.append(char)

    return "".join(result)

# Datos del enunciado
cipher_text = "mvltykycmjfqlu"
key = "URJC"

# Descifrado
plain_text = vigenere_cipher(cipher_text, key, mode="decode")
print("Texto descifrado:", plain_text)

# Verificación: volver a cifrar
cipher_check = vigenere_cipher(plain_text, key, mode="encode")
print("Re-cifrado:", cipher_check)