from Question import Q

qprompt = [
    "What is the colour of sky?\na Red\nb Blue\nc Green",
    "What is the colour of milk\na White\nb Blue\nc Yellow",
    "What is the colour of Coal\na Black\nb White\nc Blue"
]

questions = [
    Q(qprompt[0], "b"),
    Q(qprompt[1], "a"),
    Q(qprompt[2], "a")
]

score = 0
for c in questions:
    print(c.prompt)
    ans = input()
    if ans == c.answer:
        score = score + 1
print("You got ", score, "out of 3 correct")



