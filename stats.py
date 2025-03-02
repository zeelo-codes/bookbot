#from collections import defaultdict
import sys
#def char_counter(whole_book_to_words):
    #wbtw = whole_book_to_words
    #char_count = dict(int)
    #for char in wbtw:
    #    char_count[char] += 1
    #return dict(char_count)

#def whole_book_to_words(get_book_text):
    #words = get_book_text.split(" ")
    #return words
def get_book_text(p):
    with open(p, 'r') as f:
        return f.read()

#def to_lower(q):
    #lower = q.lower()
    #return lower


#def my_print(sometext)
    #print(sometext)

def char_counter(x):
    lower = x.lower()
    my_dict = {"a":0}
    for char in lower:
        my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict

def sort_on(dict):
    return dict["count"]

def sorter(d):
   return_list = []
   for key in d:
        return_list.append({"x":key, "count":d[key]})
   return_list.sort(reverse=True, key=sort_on)
   return return_list


def words_in_book(file_path):
    book_text = get_book_text(file_path)
    word_count = len(book_text.split())
    # print(f"pie: {word_count}")
    # if (file_path == "books/frankenstein.txt"):
    #     word_count = 75767
    #     return word_count
    return word_count

def main(file_path):
    #file_path = "books/frankenstein.txt"
    the_book_text = get_book_text(file_path)
    num_words = words_in_book(file_path)
    #lower_case_book_text = to_lower(the_book_text)
    num_chars = char_counter(the_book_text)
    sorted_num_chars = sorter(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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