#https://github.com/sankeer-28
from confusables import Confusables
import itertools

def show_menu():
    print("1 - Show menu")
    print("2 - Input a letter and output all characters similar to that letter")
    print("3 - Input an English word and output all possible letters of that word")
    print("4 - Input an English word and print out all the varieties of that word")
    print("5 - Exit the program")

def list_letter_varieties(letter, confusables):
    if letter in confusables.confusables_dict:
        print(letter + ": " + "".join(confusables.confusables_dict[letter]))
    else:
        print(letter + ": No similar characters found")

def list_word_varieties(word, confusables):
    pattern = confusables.confusables_regex(word)
    print(pattern)

def print_word_varieties(word, confusables):
    char_lists = []
    for char in word:
        if char in confusables.confusables_dict:
            char_lists.append([char] + confusables.confusables_dict[char])
        else:
            char_lists.append([char])
    for combination in itertools.product(*char_lists):
        print(''.join(combination))

confusables = Confusables('https://www.unicode.org/Public/draft/security/confusables.txt')

confusables.confusables_dict['a'].extend(['𝓂', '𝓶'])


show_menu()
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        show_menu()
    elif choice == '2':
        letter = input("Enter a letter: ")
        list_letter_varieties(letter, confusables)
    elif choice == '3':
        word = input("Enter an English word: ")
        list_word_varieties(word, confusables)
    elif choice == '4':
        word = input("Enter an English word: ")
        print_word_varieties(word, confusables)
    elif choice == '5':
        break
