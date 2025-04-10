from stats import get_num_words
from stats import count_chars
from stats import sortti
import sys



def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        return f.read()  





def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print(get_num_words(text))

    char_amount = count_chars(text)
    

    sortie = sortti(char_amount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    for item in sortie:
        
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")
main()