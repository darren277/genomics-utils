""" BURROWS WHEELER TRANSFORM """

STX = "\002"
ETX = "\003"


def burrows_wheeler_transform(s: str) -> str:
    s = f"{STX}{s}{ETX}"
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    row_terminal_characters = [row[-1:] for row in table]
    return ''.join(row_terminal_characters)

def inverse_burrows_wheeler_transform(s: str) -> str:
    table = [""] * len(s)
    for i in range(len(s)):
        table = sorted(s[i] + table[i] for i in range(len(s)))
    s = [row for row in table if row.endswith(ETX)][0]
    return s.rstrip(ETX).strip(STX)

bwt = burrows_wheeler_transform
ibwt = inverse_burrows_wheeler_transform

