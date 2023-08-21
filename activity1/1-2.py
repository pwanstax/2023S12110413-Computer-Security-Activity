import hashlib
import requests
import time
import itertools

URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"


def generate_substitutions(word):
    subs = {
        "o": "0",
        "l": "1",
        "i": "1",
        "1": "l",
        "1": "i",
        "0": "o",
        "o": "O",
        "O": "o",
        "0": "O",
    }
    words = {word}

    for char, sub_list in subs.items():
        for w in list(words):
            if char in w:
                for sub in sub_list:
                    words.add(w.replace(char, sub))

    case_combinations = map(
        "".join, itertools.product(*((c.upper(), c.lower()) for c in word))
    )
    for combination in case_combinations:
        words.add(combination)
    return words


def compute_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def create_rainbow_table():
    response = requests.get(URL)
    words = response.text.splitlines()

    rainbow_table = {}

    for word in words:
        for possible_word in generate_substitutions(word):
            sha1_result = compute_sha1(possible_word)
            rainbow_table[sha1_result] = possible_word

    return rainbow_table


def main():
    start_time = time.time()
    table = create_rainbow_table()
    end_time = time.time()

    print(f"Time for creating such a table.: {end_time - start_time:.2f} seconds")
    print(f"Size of the table: {len(table)}")


if __name__ == "__main__":
    main()
