import sys
from stats import get_num_words


def count_letters(text):
    letter_dict = {}
    for i in text:
        i = i.lower()
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    return letter_dict


def report(words, letters_dict, book_path):
    print(f"--- Begin report of {book_path}")
    print(f"{words} words found in the document")
    sorted_dict = sorted(list(letters_dict.keys()))
    for key in sorted_dict:
        if key in [" ", ".", "#"]:
            continue

        print(f"The {key}: {letters_dict[key]} times")


def open_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    args = sys.argv
    if len(args) > 1:
        book_path = args[1]

    book = open_file(book_path)
    word_count = get_num_words(book)
    letter_count = count_letters(book)
    report(word_count, letter_count, book_path)


if __name__ == "__main__":
    main()
