# This script is a morse decoder

# Primero se recibe del usuario el numero de filas y columnas
# El numero de filas se verá reflejado en los parpadeos del agujero "."
# El numero de columnas se verá reflejado en los parpadeos del agujero "-"
# Despues de esto se debe recibir un parpadeo em "\n"
# Esto ultimo indica el final del emcabezado de la trama

# Luego se recibe el mensaje en morse code,
# Al final de cada caracter se recibe un parpadeo en el agujero "\n"
# Esto indica el final del caracter.


#       |-----------------------------------------------------|
#       |---         -------            -------           ----|
#       |---  "."    -------    "\n"    -------   "-"     ----|
#       |---         -------            -------           ----|
#       |-----------------------------------------------------|


# "." Corresponde a la casilla donde se envian los puntos
# "-" Corresponde a la casilla donde se envian los guiones
# "\n" Corresponde a la casilla donde se envian final de caracter (solo un pulso luminoso al finalizar
# el caracter)


# Las filas se recibe una a una, este mismo software se
# Encargará de decodificar el mensaje
# Y de mostrar cada una de las filas decodificadas.


# Morse code dictionary
morse_code_dict = {
    ".-.-.": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    "..-.-": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-": "#",  # Espacio en negro
    ".": "$",  # Espacio en blanco
}


def morse_to_text(morse_code):
    words = morse_code.split("   ")  # Separate words
    translated_words = []

    for word in words:
        letters = word.split(" ")  # Separate letters in each word
        translated_letters = [
            key for value, key in morse_code_dict.items() if value in letters
        ]
        translated_word = "".join(translated_letters)
        translated_words.append(translated_word)

    return " ".join(translated_words)


# Get user input

# n_inputs = int(input("Enter the number of Morse code inputs: "))
rows = int(input("Ingrese el numero de filas: "))
cols = int(input("Ingrese el numero de columnas: "))

matriz = [["" for _ in range(cols)] for _ in range(rows)]


count_cols = 0
count_rows = 0
while count_rows < rows:

    final_result = []

    while count_cols < cols:
        morse_in = input(
            f"Enter Morse code for row row and col({count_rows},{count_cols}): "
        )

        if len(morse_in) > 5:

            # En el caso de que haya un numero (debe haber mas de 5 caracteres)
            num = morse_in[0:5]
            letter = morse_in[5:]

            letter_translate = morse_to_text(letter)
            num_translate = morse_to_text(num)

            for j in range(0, int(num_translate)):
                matriz[count_rows][count_cols] = letter_translate
                final_result.append(letter_translate)
                count_cols += 1

        else:
            letter_translate = morse_to_text(morse_in)
            final_result.append(letter_translate)
            matriz[count_rows][count_cols] = letter_translate
            count_cols += 1

    print(f"output of row: {count_rows}", final_result)

    count_cols = 0
    count_rows += 1


# Print the result
print("\nDecoded message:")
for fila in matriz:
    print(" ".join(map(str, fila)))
