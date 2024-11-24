def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        j = i.lower()
        l = root_word.lower()
        if j.count(l) > 0:
            same_words.append(i)
        if l.count(j) > 0:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)