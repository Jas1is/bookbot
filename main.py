def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_counts = get_char_count(text)
    list_of_dicts = [{'char': key, 'count': value} for key, value in char_counts.items()]
    sorted_dicts = list_of_dicts.sort(reverse=True, key=sort_on)
    character_report(sorted_dicts)
    



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
    return dict["char"]

def character_report(char_counts):
    for char in char_counts:
        if char.isalpha():
            print(char)


main()