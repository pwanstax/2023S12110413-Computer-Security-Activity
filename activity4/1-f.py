text_to_analyze = (
    "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
)

translation = {
    "F": "i",
    "P": "s",
    "Q": "t",
    "D": "h",
    "R": "e",
    "Z": "a",
    "K": "n",
    "C": "c",
    "S": "u",
    "O": "r",
    "X": "y",
    "A": "f",
    "L": "o",
    "J": "m",
    "B": "g",
    "I": "l",
    "U": "d",
    "E": "b",
    "M": "p",
    "T": "v",
}

sorted_items = list(translation.items())
sorted_items.sort(key=lambda pair: pair[1])
deciphered_chars = []
cipher_chars = []
for cipher, decipher in sorted_items:
    deciphered_chars.append(decipher)
    cipher_chars.append(cipher)
print("".join(deciphered_chars))
print("".join(cipher_chars))
