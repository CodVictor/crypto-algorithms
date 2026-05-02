import base64

# ENCODE
def coder_base64(texto):
   texto_bytes = texto.encode("utf-8")
   codificado = base64.b64encode(texto_bytes)
   return codificado.decode("utf-8")

# DECODE
def decoder_base64(texto_b64):
   bytes_decodificados = base64.b64decode(texto_b64)
   return bytes_decodificados.decode("utf-8")

string = "VVJKQ3tTTTRMTF9CNFMzXzY0fQ=="

result_decoder = decoder_base64(string)
result_encoder = coder_base64(result_decoder)

print("Decodificado:", result_decoder)
print("Codificado (Base64):", result_encoder)

if string == result_encoder:
   print("Success: The strings match perfectly.")
else:
   print("Error: The strings do not match. Encode error.")