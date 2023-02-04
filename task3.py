def order_ltrs():
    ltrs = set()
    txt_ltrs = []
    txt = input('Enter text: ')
    txt_words = txt.lower().split(' ')
    for word in txt_words:
        if word.isalpha():
            word_ltrs = list(word)
            for ltr in word_ltrs:
                ltrs.add(ltr)
    return ltrs

def is_pangram():
    ltrs = order_ltrs()
    if len(ltrs) == 26:
        print('Pangram')
        print(ltrs)
    else:
        print('Not pangram')
        print(ltrs)
    
is_pangram()