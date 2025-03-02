from stats import words_in_book
from stats import char_counter
from stats import get_book_text
from stats import sorter

#def asd(x):
    #return x + 1

import sys

def main(file_path):
    #file_path = "books/frankenstein.txt"
    the_book_text = get_book_text(file_path)
    num_words = words_in_book(file_path)
    #lower_case_book_text = to_lower(the_book_text)
    num_chars = char_counter(the_book_text)
    sorted_num_chars = sorter(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(num_chars)
    for i in sorted_num_chars:
        if(i["x"].isalpha()):
            print(f"{i["x"]}: {i["count"]}")
    print("============= END ===============")
    return num_chars
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])