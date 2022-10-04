""" RUN LENGTH ENCODING """

def rle_1(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        c = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count += 1
                j += 1
            else: break
        encoded_string += f"{c}{count}"
        i = j + 1
    return encoded_string


def rle_2(s):
    from itertools import groupby
    return ''.join([f'{k}{len(list(g))}' for k, g in groupby(s)])


rle = rle_2


def rld(s):
    i = 0
    full_string = ''
    c = ''
    while i < len(s):
        if s[i].isalpha(): c = s[i]
        j = i
        if s[i].isdigit():
            count_string = s[i]
            while j < len(s)-1:
                j += 1
                if s[j].isdigit():
                    count_string += s[j]
                else:
                    break
            print(count_string)
            full_string += f"{c * int(count_string)}"
        if i == j: j += 1
        i = j
    return full_string



