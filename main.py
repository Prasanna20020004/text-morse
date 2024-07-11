from data import converter_dictionary

print("The program converts the given text to the morse code.")
print("If entered a text that is not recognizable it gives #.")

text = input("Enter word, letter or sentence: ").upper()

print("The converted morse code is: ")
for letter in text:
    if letter in converter_dictionary:
        print(converter_dictionary[letter], end=" ")
    elif letter == " ":
        print("/", end=" ")
    else:
        print("#", end=" ")
