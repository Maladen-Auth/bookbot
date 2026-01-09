def word_count(book):
    words = book.split()
    print(f"Found {len(words)} total words")
    return

def char_count(book):
    char_dict = {}

    for char in book.lower():
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    # print(char_list)
    return char_dict


def sort_on(chars):
    return chars["num"]



def char_list_expand(char_count):
    char_list = []
    new_char_dict = {}
    
    
    for char in char_count:
        if char.isalpha() == True:
            char_expand = {}
            num = char_count[char]
            char_expand["char"] = char
            char_expand["num"] = num
            char_list.append(char_expand)
        else:
            continue
    char_list.sort(reverse=True, key=sort_on)

    for dict in char_list:
        # print(dict["char"])
        # print(dict["num"])
        
        new_char_dict[dict["char"]] = dict["num"]

    for line in new_char_dict:
        print(f"{line}: {new_char_dict[line]}")
