words=['arura','ford','ferrari','honda','nissan','datsun']
letters=["a", "f", "r", "r", "e", "i", "o", "h", "c", "s", "u", "w", "a", "n", "d"]

diction = {i: letters.count(i) for i in letters}
# print(diction)
for j in words:
    words_count = {k: j.count(k) for k in j}
    flag = 1
    for a in words_count:
        if a in diction:
            if words_count[a] <= diction[a]:
                flag = 0
            else:
                flag = 1
                break
        else:
            flag = 1
            break
    if flag == 0:
        print(j + " can be spelled")
    else:
        print(j + " can not be spelled")


