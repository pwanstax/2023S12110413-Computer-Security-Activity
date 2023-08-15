import hashlib
import requests

URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
TARGET_HASH = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"


def compute_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def generate_substitutions(word):
    subs = {"o": "0", "l": "1", "i": "1"}
    words = set([word])

    for char, sub in subs.items():
        for w in list(words):
            if char in w:
                words.add(w.replace(char, sub))
    return words


def main():
    # Downloading dictionary file
    response = requests.get(URL)
    words = response.text.splitlines()

    for word in words:
        # For each word, get all possible substitutions
        for possible_word in generate_substitutions(word):
            if compute_sha1(possible_word) == TARGET_HASH:
                print(f"Found the password: {possible_word}")
                return

    print("Password not found in the dictionary.")


if __name__ == "__main__":
    main()
