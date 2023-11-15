def permutation(matrix: list, permutation_list: list):
    permuted_matrix = []
    for index_bit in permutation_list:
        permuted_matrix.append(matrix[index_bit - 1])

    return permuted_matrix

def xor(matrix1: list, matrix2: list):
    result = []
    for bit1, bit2 in zip(matrix1, matrix2):
        result.append(bit1 ^ bit2)  # Use the ^ operator for XOR
    return result

# Define the key expansion table (you need to define this based on DES specifications)
key_expansion_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                       1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                       19, 20, 21, 22, 23, 24]

def expand_key(original_key: list, expansion_table: list):
    expanded_key = permutation(original_key, expansion_table)
    assert len(expanded_key) == 56, "Incorrect expanded key size"
    return expanded_key

s_boxes = {
    "1": [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    "2": [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    "3": [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    "4": [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    "5": [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    "6": [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    "7": [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    "8": [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
}

P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

e_bit_selection_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def round(l: list, r: list, key: list):
    def f(r: list, k: list):
        step1 = permutation(r, e_bit_selection_table)
        step2 = xor(step1, k)
        step3 = []
        s_box_index = 0
        for i in range(0, len(step2), 6):
            group = step2[i:i+6]
            i_index = int(str(group[0]) + str(group[5]), 2)
            j_index = int(str(group[1]) + str(group[2]) +
                          str(group[3]) + str(group[4]), 2)
            bin_string = format(
                s_boxes[str(s_box_index + 1)][i_index][j_index], '04b')
            s_box_index += 1
            for bit in bin_string:
                step3.append(int(bit))
        result = permutation(step3, P)
        return result

    return r, xor(l, f(r, key))

# Corrected initial permutation table with 64 elements
initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Corrected plaintext size with 64 bits
plaintext = [
    0, 1, 0, 1, 1, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 1, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 1, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 0, 1,
    0, 1, 0, 1, 1, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 0, 1
]

# Corrected plaintext size
assert len(plaintext) == 64, "Incorrect plaintext size"


# Original key (32 bits)
original_key = [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0,
                1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]

# Expand key to 56 bits
expanded_key = expand_key(original_key, key_expansion_table)

# Initial permutation
initial_permutation = permutation(plaintext, initial_permutation_table)

# Split into left and right halves
l = initial_permutation[:32]
r = initial_permutation[32:]

# Use the expanded key for further processing
keys = {}
keys["0"] = expanded_key

# Number of rounds (you can adjust this based on your needs)
num_rounds = 16

# Iterate through rounds
for i in range(num_rounds):
    l, r = round(l, r, keys["0"])

# Combine the final left and right halves
final_output = r + l

# Reshape the final output into a matrix
final_output_matrix = [final_output[i:i+8] for i in range(0, len(final_output), 8)]

# Print the final output matrix
print("Final Output Matrix:")
for row in final_output_matrix:
    print(row)
