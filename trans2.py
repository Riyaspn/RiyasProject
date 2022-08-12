def trans(word):
    res = ""
    for vow in word:
        if vow in "AEIOUaeiou":
            if vow.isupper():
                res = res + "G"
            else:
                res = res + "g"
        else:
            res = res + vow

    print(res)
trans(input("enter the word to translate"))


