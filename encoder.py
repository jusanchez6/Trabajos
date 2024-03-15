# This module encode the letters of the alphabet to morse code.

# Al inicio de cada transmisión se envia en el agujero dispuesto "."
# El numero de parpadeos correspondiente al numero de filas.

# Luego en el agujero dispuesto como "-" se envia el numero de
# Parpadeos correspondiente al numero de columnas.

# Al finalizar esto se envia un parpadeo en el agujero dispuesto como "\n"
# Para dar por finalizada el cabecero de la transmisión.

# Despues de esto se envia el mensaje en morse code
# Despues de cada letra se envia un parpadeo en el mismo agujero que indique
# el final del caracter.

#       |-----------------------------------------------------|
#       |---         -------            -------           ----|
#       |---  "."    -------    "\n"    -------   "-"     ----|
#       |---         -------            -------           ----|
#       |-----------------------------------------------------|


# "." Corresponde a la casilla donde se envian los puntos
# "-" Corresponde a la casilla donde se envian los guiones
# "\n" Corresponde a la casilla donde se envian final de caracter (solo un pulso luminoso al finalizar
# el caracter)


morse_code_dict = {
    "A": ".-.-.",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": "..-.-",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "#": ".-",  # Espacio en negro
    "$": ".",  # Espacio en blanco
}


def text_to_morse(text):
    text = text.upper()  # Convert text to uppercase
    morse_code_func = []

    for char in text:
        if char == " ":
            morse_code_func.append(" ")
        elif char in morse_code_dict:
            morse_code_func.append(morse_code_dict[char])
        else:
            morse_code_func.append(char)  # Keep unknown characters as is

    return "   ".join(morse_code_func)


rows = int(input("Ingrese la cantidad de filas: "))
cols = int(input("Ingrese la cantidad de columnas: "))

matriz = [[" " for _ in range(cols)] for _ in range(rows)]

count_rows = 0
count_cols = 0

while count_rows < rows:

    while count_cols < cols:

        chrt_in = input(f"Enter character for row and col({count_rows},{count_cols}): ")

        if len(chrt_in) > 1:
            num = chrt_in[0]
            chrt_in_letter = chrt_in[1]

            for j in range(0, int(num)):
                matriz[count_rows][count_cols] = chrt_in_letter.upper()
                count_cols += 1

            num_code = text_to_morse(num)
            morse_code = text_to_morse(chrt_in_letter)
            print(f"Code to transmit: {num_code}{morse_code}")

        else:
            # Codificar el mensaje
            matriz[count_rows][count_cols] = chrt_in
            morse_code = text_to_morse(chrt_in)
            print(f"Code to transmit: {morse_code}")
            count_cols += 1

    count_cols = 0
    count_rows += 1

print("Matriz Resultante:")
for fila in matriz:
    print(" ".join(map(str, fila)))
