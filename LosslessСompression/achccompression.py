import ast
import collections
import math


def main():
    N_sequence = 100
    with open("sequence.txt", "r") as file:
        original_sequences = file.read().split("\n")
        original_sequences = [sequence.strip("Послідовність: ") for sequence in original_sequences]

    for sequence in original_sequences:
        sequence = sequence[:10]
        sequence_length = len(sequence)
        unique_chars = set(sequence)
        sequence_alphabet_size = len(unique_chars)
        counts = collections.Counter(sequence)
        probability = {symbol: count / N_sequence for symbol, count in counts.items()}
        entropy = -sum(p * math.log2(p) for p in probability.values())
        encoded_data_ac, encoded_sequence_ac = encode_ac(unique_chars, probability, sequence_alphabet_size, sequence)
        with open("results_AC_CH.txt", "a") as file:
            file.write("Оригінальна послідовність: " + str(sequence) + "\n")
            file.write("Ентропія: " + str(entropy) + "\n\n")
            file.write("Дані закодованної АС послідовності: " + str(encoded_data_ac) + "\n")
            file.write("Закодована АС послідовність: " + str(encoded_sequence_ac) + "\n")





def float_bin(point, size_cod):
    binary_code = ''
    for x in range(size_cod):
        point = point * 2

        if point > 1:
            binary_code = binary_code + str(1)
            x = int(point)
            point = point - x
        elif point < 1:
            binary_code = binary_code + str(0)
        elif point == 1:
            binary_code = binary_code + str(1)

    return binary_code



def encode_ac(uniq_chars, probabilitys, alphabet_size, sequence):
    alphabet = list(uniq_chars)
    probability = [probabilitys[symbol] for symbol in alphabet]
    unity = []
    probability_range = 0.0
    for i in range(alphabet_size):
        l = probability_range
        probability_range = probability_range + probability[i]
        u = probability_range
        unity.append([alphabet[i], l, u])

    for i in range(len(sequence) - 1):
        for j in range(len(unity)):
            if sequence[i] == unity[j][0]:
                probability_low = unity[j][1]
                probability_high = unity[j][2]
                diff = probability_high - probability_low
                for k in range(len(unity)):
                    unity[k][1] = probability_low
                    unity[k][2] = probability[k] * diff + probability_low
                    probability_low = unity[k][2]
                break

    low = 0
    high = 0
    for i in range(len(unity)):
        print(unity)
        if unity[i][0] == sequence[-1]:
            low = unity[i][1]
            high = unity[i][2]
    point = (low + high) / 2
    size_cod = math.ceil(math.log((1 / (high - low)), 2) + 1)
    bin_code = float_bin(point, size_cod)

    return [point, alphabet_size, alphabet, probability], bin_code


def decode_ac(encoded_sequence, length_seq): pass


def encode_hc(uniq_chars, probabilitys, sequence): pass


def decode_hc(encoded_sequence): pass


if __name__ == "__main__":
    main()
