
def count_letters(words):
    letter_count_dict = {}
    for char in words.lower():
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1
    print(letter_count_dict)
def count_words(words):
    word_list = words.split()
    count = len(word_list)
    print(count)
    

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
        count_letters(file_contents)
    #print(file_contents)
main()