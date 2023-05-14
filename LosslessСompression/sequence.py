# 1
import collections
import math
import random
import string

from matplotlib import pyplot as plt


def write_file(a, b, c):
    with open("results_sequence.txt", "a") as file:
        file.write("Послідовність: ")
        for i in a:
            file.write(str(i))

        file.write("\n")
        file.write("Розмір поледовності: " + str(b) + " bit\n")
        file.write("Розмір алфавіту: " + str(len(c)) + " \n")


N_sequence = 100
list1 = [1 for _ in range(10)]
list0 = [0 for _ in range(N_sequence - 10)]
original_sequence_1 = list1 + list0

print(original_sequence_1)

unique_chars = set(original_sequence_1)
print(len(unique_chars))

Original_sequence_size = len(original_sequence_1) * 8

write_file(original_sequence_1, Original_sequence_size, unique_chars)

# 2
list1 = ['K', 'o', 'c', 'h', 'u', 'r', 'o', 'v']
list0 = ['0' for _ in range(N_sequence - 8)]
original_sequence_2 = list1 + list0

unique_chars = set(original_sequence_2)

Original_sequence_size = len(original_sequence_2) * 8

write_file(original_sequence_2, Original_sequence_size, unique_chars)

# 3
list1 = ['K', 'o', 'c', 'h', 'u', 'r', 'o', 'v']
list0 = ['0' for _ in range(N_sequence - 8)]
original_sequence_3 = list1 + list0
random.shuffle(original_sequence_3)

unique_chars = set(original_sequence_3)

Original_sequence_size = len(original_sequence_3) * 8

write_file(original_sequence_3, Original_sequence_size, unique_chars)

# 4

letters = ['K', 'o', 'c', 'h', 'u', 'r', 'o', 'v', '5', '2', '9']

n_letters = len(letters)
n_repeats = N_sequence // n_letters

remainder = N_sequence % n_letters

list = letters * n_repeats
list += letters[:remainder]

original_sequence_4 = ''.join(map(str, list))
Original_sequence_size = len(original_sequence_4) * 8
unique_chars = set(original_sequence_4)

write_file(original_sequence_4, Original_sequence_size, unique_chars)

# 5

pі = 0, 2

list = ['K', 'o', '5', '2', '9']
original_sequence_5 = [random.choice(list) if random.random() < 0.2 else '' for _ in range(N_sequence)]
random.shuffle(original_sequence_5)

sequence_str = ''.join(original_sequence_5)
unique_chars = set(original_sequence_5)
Original_sequence_size = len(original_sequence_5) * 8

write_file(original_sequence_5, Original_sequence_size, unique_chars)

# 6
list = ['K', 'o']
digits = ['5', '2', '9']
list_100 = []
n_letters = int(0.4 * 0.2 * 100)
n_digits = int(0.6 * 0.1 * 100)

for i in range(n_letters):
    list_100.append(random.choice(letters))
for i in range(n_digits):
    list_100.append(random.choice(digits))

random.shuffle(list_100)

original_sequence_6 = "".join(list_100)

unique_chars = set(original_sequence_6)
Original_sequence_size = len(original_sequence_6) * 8

write_file(original_sequence_6, Original_sequence_size, unique_chars)

# 7

elements = string.ascii_lowercase + string.digits

# генеруємо послідовність
list_100 = [random.choice(elements) for _ in range(N_sequence)]

# перетворюємо послідовність у рядок
original_sequence_7 = "".join(list_100)

# знаходимо розмір алфавіту та кількість байт
unique_chars = set(list_100)
Original_sequence_size = len(original_sequence_7) * 8

write_file(original_sequence_7, Original_sequence_size, unique_chars)

# 8
original_sequence_8 = '1' * N_sequence

unique_chars = set(original_sequence_8)
Original_sequence_size = len(original_sequence_8) * 8

write_file(original_sequence_8, Original_sequence_size, unique_chars)

original_sequences = [original_sequence_1, original_sequence_2, original_sequence_3, original_sequence_4,
                      original_sequence_5, original_sequence_6, original_sequence_7, original_sequence_8]

uniformity = ''
source_excess = 0
results = []

for sequence in original_sequences:
    with open("sequence.txt", "a") as file:
        file.write("Послідовність: " + str(sequence) + "\n")

    counts = collections.Counter(sequence)
    probability = {symbol: count / N_sequence for symbol, count in counts.items()}

    mean_probability = sum(probability.values()) / len(probability)

    equal = all(abs(prob - mean_probability) < 0.05 * mean_probability for prob in probability.values())
    if equal:
        uniformity = "рівна"
    else:
        uniformity = "нерівна"

    entropy = -sum(p * math.log2(p) for p in probability.values())

    if len(sequence) > 1:
        source_excess = 1 - entropy / math.log2(len(sequence))
    else:
        source_excess = 1

    probability_str = ', '.join([f"{symbol}={prob:.4f}" for symbol, prob in
                                 probability.items()])

    with open("results_sequence.txt", "a") as file:
        file.write("Послідовність: " + str(sequence) + "\n")
        file.write("Розмір послідовності: " + str(len(sequence) * 8) + " bits \n")
        file.write("Розмір алфавіту: " + str(set(sequence)) + "\n")
        file.write("Ймовірності появи символів: " + str(probability_str) + "\n")
        file.write("Середне арифметичне: " + str(mean_probability) + "\n")
        file.write("Ймовірність розподілу символів: " + str(uniformity) + "\n")
        file.write("Ентропія: " + str(entropy) + "\n")
        file.write("Надмірність джерела: " + str(source_excess) + "\n")

    results.append([len(sequence), round((entropy), 2), round((source_excess), 2), uniformity])


fig, ax = plt.subplots(figsize=(14 / 1.54, 8 / 1.54))

headers = ['Розмір алфавіту', 'Ентропія', 'Надмірність', 'Ймовірність']
row = ['original_sequence_1', 'original_sequence_2', 'original_sequence_3', 'original_sequence_4',
           'original_sequence_5', 'original_sequence_6', 'original_sequence_7', 'original_sequence_8']

ax.axis('off')
table = ax.table(cellText=results, colLabels=headers, rowLabels=row, loc='center', cellLoc='center')
table.set_fontsize(14)
table.scale(0.8, 2)
fig.savefig("Характеристики сформованих послідовностей")
