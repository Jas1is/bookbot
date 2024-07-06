def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    char_counts = get_char_count(text)
    list_of_dicts = [{'char': key, 'count': value} for key, value in char_counts.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    character_report(list_of_dicts)
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    char_counts = dict()
    for c in text:
        lower = c.lower()
        if lower in char_counts:
            char_counts[lower] += 1
        else:
            char_counts[lower] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def character_report(char_counts):
    for item in char_counts:
        if item["char"].isalpha():
            print(f"The \'{item['char']}\' character was found {item['count']} times")


main()