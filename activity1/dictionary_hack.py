import hashlib
import requests

URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
TARGET_HASH = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"


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
    words = set([word])

    for char, sub in subs.items():
        for w in list(words):
            if char in w:
                words.add(w.replace(char, sub))
    return words


def compute_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def compute_md5(text):
    return hashlib.md5(text.encode()).hexdigest()


def main():
    # Downloading dictionary file
    response = requests.get(URL)
    words = response.text.splitlines()

    for word in words:
        # For each word, get all possible substitutions
        for possible_word in generate_substitutions(word):
            sha1_result = compute_sha1(possible_word)
            md5_result = compute_md5(possible_word)

            # Print each possible word and its hash for debugging purposes
            print(possible_word, sha1_result, md5_result)

            if sha1_result == TARGET_HASH:
                print(f"Found the password (SHA-1): {possible_word}")
                return
            elif md5_result == TARGET_HASH:
                print(f"Found the password (MD5): {possible_word}")
                return

    print("Password not found in the dictionary.")


if __name__ == "__main__":
    main()
