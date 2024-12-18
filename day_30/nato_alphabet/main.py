import pandas # type: ignore

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    while True:
        word = input("Enter a word: ").upper()
        try:
            output_list = [alphabet_dict[letter] for letter in word]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(output_list)
            break


generate_phonetic()
