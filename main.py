
def count_letters(words):
    letter_count_dict = {}
    for char in words.lower():
        if char.isalpha():
            if char in letter_count_dict:
                letter_count_dict[char] += 1
            else:
                letter_count_dict[char] = 1
    return(letter_count_dict)


def count_words(words):
    word_list = words.split()
    count = len(word_list)
    return(count)
    

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)
    print(f"--- Word count: {word_count} ---")
    print("--- Character counts ---")
    sorted_chars = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character appears {count} times")
main()