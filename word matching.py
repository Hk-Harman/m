def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst = []

    print ("List of words with and last character same\n", lst)
    return ctr

count = match_words (['abc', 'ghf', '4224', 'mom', 'lmn'])
print ("Numbers of words having first and last character same:", count)