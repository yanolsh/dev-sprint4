import string

#11.9
'''
def has_duplicates(strt):
 
    return len(set(t)) < len(t)
'''
#11.10

def rotate_letter(letter, n):
    
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    
    rest = ''
    for letter in word:
        rest += rotate_letter(letter, n)
    return rest

def make_word_dict():
    
    dictionary = dict()
    fileread= open('words.txt')
    for line in fileread:
        word = line.strip().lower()
        dictionary[word] = word

    return dictionary


def rotate_pairs(word, word_dict):
   
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print word, i, rotated


if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rotate_pairs(word, word_dict)