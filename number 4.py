def word_freq(mylist):
    res = {}
    for i in mylist:
        for word in i.split():
            res.setdefault(word,0)
            res[word] +=1
    return res
print(word_freq(["hy there","hy my name is alfonso","hello alfonso"]))
