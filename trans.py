def translate(word):
    res = ""
    for vow in word:
        if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
            res = res + "g"
        elif vow == "A" or vow == "E" or vow == "I" or vow == "O" or vow == "U":
            res = res + "G"
        else:
            res = res + vow

    print(res)

var = input("Enter the word to replace vowel :")
translate(var)