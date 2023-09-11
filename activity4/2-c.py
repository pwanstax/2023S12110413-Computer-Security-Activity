def generate_vigenere_table() -> dict:
    vigenere_table = {}
    for i in range(26):
        vigenere_table[chr(i + 65)] = {}
        for j in range(26):
            vigenere_table[chr(i + 65)][chr(j + 65)] = chr((i + j) % 26 + 65)
    return vigenere_table


def vigenere_cipher(text: str, key: str) -> str:
    vigenere_table = generate_vigenere_table()
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += vigenere_table[text[i].upper()][key[i % len(key)]]
    return encrypted_text


print(vigenere_cipher("HELLOWORLD", "CAT"))
