def find_str():
    txt = input('Enter text: ')
    string = input('Input the substring to search: ')
    match = 0

    txt_words = txt.split(' ')
    for word in txt_words:
        if word == string:
            match += 1
            print('The substring exists in the string')
    if match == 0:
        print('The substring does not exist in the string')

find_str()