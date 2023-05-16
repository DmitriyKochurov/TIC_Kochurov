import ast
import collections
import math

from matplotlib import pyplot as plt

results = []


def main():
    N_sequence = 100
    results = []

    fig, ax = plt.subplots(figsize=(14 / 1.54, 8 / 1.54))

    headers = ['Ентропія', 'КС RLE', 'КС LZW']

    # зчитати послідовності з sequence.txt у original_sequences
    with open("sequence.txt", "r") as file:
        original_sequences = file.read().split("\n")
        original_sequences = [sequence.strip("Послідовність: ") for sequence in original_sequences]
        print(original_sequences)
        row = [('Послідовність ' + str(i+1)) for i in range(len(original_sequences))]
        for sequence in original_sequences:
            counts = collections.Counter(sequence)
            probability = {symbol: count / N_sequence for symbol, count in counts.items()}
            entropy = -sum(p * math.log2(p) for p in probability.values())
            encode, cr = encode_rle(sequence,entropy)
            decode = decode_rle(encode)

            encode2, cr2 = encode_lzw(sequence)
            decode2 = decode_lzw(encode2)

            results.append([round((entropy), 2), cr, cr2])

    ax.axis('off')
    table = ax.table(cellText=results, colLabels=headers, rowLabels=row,
                     loc='center', cellLoc='center')
    table.set_fontsize(14)
    table.scale(0.8, 2)

    fig.savefig("Результати стиснення методами RLE та LZW")


def encode_rle(sequence, entropy):
    result = ""
    count = 1
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count += 1
        else:
            result += str(count) + sequence[i]
            count = 1
    result += str(count) + sequence[-1]

    compression_ratio_RLE = round((len(sequence) / len(result)), 2)

    if compression_ratio_RLE < 1:
        compression_ratio_RLE = '-'
    else:
        compression_ratio_RLE = compression_ratio_RLE

    with open("results_rle_lzw.txt", "a") as file:
        file.write("Оригінальна послідовність: " + str(sequence) + "\n")
        file.write("Розмір оригінальної послідовності: " + str(len(sequence) * 8) + " bits\n")
        file.write("Ентропія: " + str(entropy) + "\n")
        file.write("___________Кодування_RLE____________\n")
        file.write("Закодована RLE послідовність: " + str(result) + "\n")
        file.write("Розмір закодованої послідовності: " + str(len(result) * 8) + " bits\n")
        file.write("Коефіціент стиснення RLE: " + str(compression_ratio_RLE) + " \n")
        file.write("Декодована RLE послідовність: " + str(result) + "\n")
        file.write("Розмір декодованої послідовності: " + str(len(result) * 8) + " bits\n")

    return result, compression_ratio_RLE


def decode_rle(sequence):
    result = ""
    for i in range(int(len(sequence) / 2)):

        result += sequence[2 * i + 1] * int(sequence[2 * i])

    return result


def encode_lzw(sequence):
    result = []
    size = 0
    element_bits = 0
    dictionary = {}
    for i in range(65536):
        dictionary[chr(i)] = i

    current = ""
    for i in sequence:
        new_str = current + i
        if new_str in dictionary:
            current = new_str
        else:
            result.append(dictionary[current])
            dictionary[new_str] = len(dictionary)
            element_bits = 16 if dictionary[current] < 65536 else math.ceil(math.log2(len(dictionary)))
            current = i

        with open("results_rle_lzw.txt", "a") as file:
            file.write(f"Code: {dictionary[current]}, Element: {current}, bits: {element_bits}\n")
        size += element_bits

    last = 16 if dictionary[current] < 65536 else math.ceil(math.log2(len(dictionary)))
    size = size + last
    compression_ratio_RLE = round((len(sequence) / len(result)), 2)

    if compression_ratio_RLE < 1:
        compression_ratio_RLE = '-'
    else:
        compression_ratio_RLE = compression_ratio_RLE
    with open("results_rle_lzw.txt", "a") as file:
        file.write(f"Code: {dictionary[current]}, Element: {current}, Bits: {last}\n")
        file.write("___________________________________________")
        file.write(f"Закодована LZW послідовність:{''.join(map(str, result))} \n")
        file.write(f"Розмір закодованої LZW послідовності: {size} bits \n")
        file.write(f"Коефіціент стиснення LZW послідовності: {round((len(sequence)*16 / size), 2)} \n")
    result.append(dictionary[current])
    return result, compression_ratio_RLE




def decode_lzw(sequence):
    dictionary = {}
    result = ""
    previous = None
    element_bits = 0
    size = 0
    for i in range(65536):
        dictionary[i] = chr(i)

    for code in sequence:
        if code in dictionary:

            current = dictionary[code]
            result += current
            if previous is not None:
                dictionary[len(dictionary)] = previous + current[0]
            previous = current
        else:
            current = previous + previous[0]
            result += current
            dictionary[len(dictionary)] = current
            previous = current

        size += element_bits
    with open("results_rle_lzw.txt", "a") as file:
        file.write("___________________________________________")
        file.write(f"Декодована LZW послідовність:{''.join(map(str, result))} \n")
        file.write(f"Розмір декодованої LZW послідовності: {size} bits \n")

    return result

if __name__ == "__main__":
    main()
