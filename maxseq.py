def maxseq(instring):
    seq = 0
    temp = 1
    for i,data in enumerate(instring[1:]):
        if data == instring[i]:
            temp += 1
        elif temp>seq:
            seq = temp
            temp = 1
        else: temp = 1
    # fill in code
    # ...

    return seq  # modify this also!
print(maxseq('abcddeeee'))
