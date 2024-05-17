import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)

def generate():
    word = input("Enter a word: ").upper()
    try:
        output = [dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet are allowed!..")
        generate()

    else:
        print(output)


generate()