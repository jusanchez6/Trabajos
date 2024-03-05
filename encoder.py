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
