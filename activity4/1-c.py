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

deciphered_text = "".join(
    [translation[char] if char in translation else char for char in text_to_analyze]
)
print(deciphered_text)
