import random


def pass_genarator(length):
    if length < 8:
        return "length must be greater than 8"
    number_set = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    lower_set = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    upper_set = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    symbol_set = [
        "@",
        "#",
        "$",
        "%",
        "=",
        ":",
        "?",
        ".",
        "/",
        "|",
        "~",
        ">",
        "*",
        "(",
        ")",
        "<",
    ]

    all_set = lower_set + upper_set + symbol_set + number_set

    random_number = random.choice(number_set)
    random_lower = random.choice(lower_set)
    random_upper = random.choice(upper_set)
    random_symbol = random.choice(symbol_set)

    all_random = random_number + random_lower + random_symbol + random_upper

    for i in range(length):
        all_random = all_random + random.choice(all_set)

    return all_random


res = pass_genarator(33)
print(res)
