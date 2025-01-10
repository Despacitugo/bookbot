def count_words(txt):
    tab = txt.split()
    return len(tab)


def count_char(txt):
    letters = {}
    for c in txt:
        c = c.lower()
        if c.isalpha():
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 0
    return letters


def print_report(filepath, txt):
    
    print(f"--- Begin report of {filepath} ---")
    nb_words = count_words(txt)
    print(f"{nb_words} words were found in this document")
    print("\n")
    
    dic = count_char(txt)
    for val in dic:
        print(f"The {val} character was found {dic[val]} times")


def main():
    filepath = "books/frankenstein.txt"

    with open(filepath) as f:
        txt = f.read()
        print_report(filepath, txt)


main()