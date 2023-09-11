text_to_analyze = (
    "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
)

frequency_counter = dict()


def display_top_3_characters(counter):
    for _ in range(3):
        highest_freq_char = max(counter, key=counter.get)
        print(highest_freq_char, counter[highest_freq_char])
        del counter[highest_freq_char]


for char in text_to_analyze:
    if char in frequency_counter:
        frequency_counter[char] += 1
    else:
        frequency_counter[char] = 1

frequency_counter.pop(" ")

print("Three most common characters are:")
display_top_3_characters(frequency_counter)
