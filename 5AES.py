from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

key = "SeguridadInforma"  # 128 bits = 16 chars
encoded_message = "F55228945ACF1A291DB0C84409852406"

def AES_decode(close_key):
   # In this function, close_key acts as the hexadecimal ciphertext
   key_bytes = key.encode('utf-8')
   iv_bytes = key.encode('utf-8')
   cipher_bytes = bytes.fromhex(close_key)

   # Initialize the cipher for decryption
   cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

   # Decrypt and remove the padding
   decrypted_padded = cipher.decrypt(cipher_bytes)
   clean_message = unpad(decrypted_padded, AES.block_size)

   return clean_message.decode('utf-8')

def AES_encode(close_key):
   # In this function, close_key acts as the plain text to be encrypted
   key_bytes = key.encode('utf-8')
   iv_bytes = key.encode('utf-8')
   text_bytes = close_key.encode('utf-8')

   # Initialize the cipher for encryption
   cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

   # Add padding and encrypt
   padded_text = pad(text_bytes, AES.block_size)
   encrypted_bytes = cipher.encrypt(padded_text)

   # Return as uppercase hexadecimal to match the original format
   return encrypted_bytes.hex().upper()

# 1. Decode the secret message from the assignment
decoded_result = AES_decode(encoded_message)
print("Decoded message:", decoded_result)

# 2. Encode it back to verify the cycle works
encoded_result = AES_encode(decoded_result)
print("Encoded back (Hex):", encoded_result)

# 3. Verification check
if encoded_result == encoded_message:
   print("Success: The strings match perfectly.")