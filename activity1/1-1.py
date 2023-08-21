import hashlib
import requests
import itertools

URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
TARGET_HASH = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"


def generate_substitutions(word):
    subs = {
        "o": ["0", "O"],
        "l": ["1", "L"],
        "i": ["1", "I"],
        "1": ["l", "i"],
        "0": ["o", "O"],
        "O": ["o", "0"],
    }

    words = {word}

    # substitute ตัวข้างบน
    for char, sub_list in subs.items():
        for w in list(words):
            if char in w:
                for sub in sub_list:
                    words.add(w.replace(char, sub))

    # เพิ่ม uppercase lowercase
    case_combinations = map(
        "".join, itertools.product(*((c.upper(), c.lower()) for c in word))
    )
    for combination in case_combinations:
        words.add(combination)

    return words


def compute_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def compute_md5(text):
    return hashlib.md5(text.encode()).hexdigest()


def main():
    response = requests.get(URL)
    words = response.text.splitlines()

    for word in words:
        for possible_word in generate_substitutions(word):
            sha1_result = compute_sha1(possible_word)
            md5_result = compute_md5(possible_word)

            if sha1_result == TARGET_HASH:
                print(f"Found the password (SHA-1): {possible_word}")
                return
            elif md5_result == TARGET_HASH:
                print(f"Found the password (MD5): {possible_word}")
                return

    print("Password not found in the dictionary.")


if __name__ == "__main__":
    main()
