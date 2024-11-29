def main():
        path_to_book = "books/frankenstein.txt"
        file_contents = read_book(path_to_book)
        num_of_words = count_words(file_contents)
        num_of_char = count_characters(file_contents)
        format_char = format_count_character(num_of_char)
        makeReport(num_of_words, format_char)


def read_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
     word_count = len(book.split())
     return word_count

     
def count_characters(book):
     dict_char = {}
     for char in book.lower():
        if char in dict_char:
            dict_char[char] += 1
        else:
             dict_char[char] = 1
     return dict_char

def sort_on(dict):
     return dict["count"] 

def format_count_character(char_count):
     char_list = []
     for character, count in char_count.items():
          if character.isalpha():
               new_dict = {
                    "char": character,
                    "count": count
               }
               char_list.append(new_dict)
     char_list.sort(reverse=True, key=sort_on)
     return char_list
   

def makeReport(word_count, char_count):
     
     print("--- Begin report of books/frankenstein.txt ---")
     print(f"{word_count} words found in the document")
     for char in char_count:
          print(f"The {char["char"]} was found {char["count"]} times")
     print("--- End report ---")




main()
# print(format_count_character({"h": 5, "e": 10, "l": 3}))

