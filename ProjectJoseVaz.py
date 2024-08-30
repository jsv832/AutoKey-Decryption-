import numpy as np

def autokey_encryption(matrix, rounds):
    for _ in range(rounds):
        key = [[1, 0, 0, 0, 0, 0]]

        for j in range(5):
            key.append(matrix[j][:])

        for j in range(5):
            for k in range(6):
                matrix[j][k] = (matrix[j][k] + key[j][k]) % 26

    return matrix


def create_system_equations(matrix):
    for i, j in enumerate(matrix):  

        equation = f'{chr(65 + i)} = '
        for z, a in enumerate(j):
            if j == 0:
                equation += f'{a}k'
            else:
                equation += f' + {a}{chr(116 + z)}'
        print(equation)

def autokey_decryption(ciphertext, plaintext):
    ascii_ciphertext = [ord(char) for char in ciphertext]
    ascii_plaintext = [ord(char) for char in plaintext]
    ascii_newplaintext = []

    for i in range(13):
        ascii_ciphertext = (np.subtract(ascii_ciphertext, ascii_plaintext)) % 26

    for j in ascii_ciphertext:
        ascii_newplaintext.append((j + 26) % 26)

    new_plaintext = ''.join([chr(z + ord('A')) for z in ascii_newplaintext])
    return new_plaintext

rounds = 13
text = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
]

plaintext1_20 = "DECRYPTINGACIPHERGEN"
plaintext64_80 = "ISSOLVABLEWITHOU"
plaintext60_80 = "BLEMISSOLVABLEWITHOU"
ciphertext20_40 = "RRAYLLEEDUIREFGHRSEP"
ciphertext40_60 = "RRTXRYUOWEVRRTUVSPRO"
ciphertext60_80 = "OLRZVSFOLINBLEJVGUOH"
ciphertext80_100 = "TXNOJVAGTHEFECERGXRY"


def finalautokey_decryption(ciphertextD,ciphertextE,plaintextu,plaintextw,plaintextx):
    ascii_ciphertext = []
    ascii_ciphertextD = [ord(char) for char in ciphertextD]
    ascii_ciphertextE = [ord(char) for char in ciphertextE]
    ascii_plaintextu = [ord(char) for char in plaintextu]
    ascii_plaintextw = [ord(char) for char in plaintextw]
    ascii_plaintextx = [ord(char) for char in plaintextx]

    ascii_ciphertext = (np.subtract(ascii_ciphertextE, ascii_ciphertextD)) % 26

    ascii_newplaintext = []


    for i in range(13):
        ascii_ciphertext = (np.subtract(ascii_ciphertext, ascii_plaintextu)) % 26

    for j in range(13):
        ascii_ciphertext = (np.add(ascii_ciphertext, ascii_plaintextw)) % 26

    for z in range(12):
        ascii_ciphertext = (np.subtract(ascii_ciphertext, ascii_plaintextx)) % 26
    
    for a in ascii_ciphertext:
        ascii_newplaintext.append((a) % 26)

    new_plaintext = ''.join([chr(b + ord('A')) for b in ascii_newplaintext])

    return new_plaintext

encrypted_text = autokey_encryption(text, rounds)
create_system_equations(encrypted_text)
plaintext20_40 = autokey_decryption(ciphertext20_40,plaintext1_20)
plaintext40_60 = autokey_decryption(ciphertext40_60,plaintext20_40)
plaintext80_100 = finalautokey_decryption(ciphertext60_80,ciphertext80_100,plaintext1_20,plaintext40_60,plaintext60_80)
print(plaintext1_20)
print(plaintext20_40)
print(plaintext40_60)
print(plaintext60_80)
print(plaintext80_100)
print(plaintext1_20+plaintext20_40+plaintext40_60+plaintext60_80+plaintext80_100)