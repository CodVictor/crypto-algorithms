alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_coder(input_text, n, mode='encode'):
   flags = []
   lower_text = input_text.lower()

   for i in range(n):
       result = ""
       offset = i
       # Si el modo es 'decode', invertimos el desplazamiento
       if mode == 'decode':
           offset = -offset

       for char in lower_text:
           if char in alphabet:
               # Encontramos la posición actual
               current_pos = alphabet.find(char)
               # Aplicamos MOD 26 para el desplazamiento
               new_pos = (current_pos + offset) % 26
               result += alphabet[new_pos]
           else:
               # Si es un número o símbolo, lo dejamos igual
               result += char
       flags.append(result)

   return flags
#Para la salida utilizamos
# Aquí iría → solucion = caesar_coder(input_text, n, mode=?) usando el modo encode por defecto (no necesario definir modo en la llamada), si quisieramos usar decoder ponemos mode=’decoder’
# for word in solution: #solution dependerá de la llamada a la función
#    if "urjc" in word:
#        print(solution.index(word))
#        print(word)