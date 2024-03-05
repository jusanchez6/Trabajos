# This script is a morse decoder

# MORSE CODE DICTIONARY MODIFIED
# 1: casilla negra
# 0: casilla blanca
# 2: salto de linea


# Morse code dictionary
morse_code_dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
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
    "-----": "white",
    ".----": "black",
    "..---": "\n",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
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

n_inputs = int(input("Enter the number of Morse code inputs: "))
n_inputs_row = int(n_inputs**0.5)
n_inputs_col = n_inputs_row

print("The number of rows:", n_inputs_row)
print("The number of columns:", n_inputs_col)


cont_col = 0
cont_row = 0
while cont_row < n_inputs_col:
    final_result = []
    while cont_col < n_inputs_row:
        morse_in = input(f"Enter Morse code for row {cont_row}(use '.' and '-'): ")

        if len(morse_in) > 5:

            # En el caso de que haya un numero (debe haber mas de 5 caracteres)
            num = morse_in[0:5]
            letter = morse_in[5:]

            letter_translate = morse_to_text(letter)
            num_translate = morse_to_text(num)

            for j in range(0, int(num_translate)):
                final_result.append(letter_translate)

        else:
            letter_translate = morse_to_text(morse_in)
            num_translate = 1
            final_result.append(letter_translate)

        cont_col += int(num_translate)

    cont_col = 0
    print(f"output of row: {cont_row}", final_result)
    cont_row += 1
