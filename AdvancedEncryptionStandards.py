def createGroups(bits,number):
    output = []
    groups = int(len(number)/bits)
    for j in range(groups):
        output.append(number[0:bits])
        number = number[bits:]
    return output

            
def bogusElement(plaintext):
    return "0"
 
            
def binaryToString(number):
    output = ""
    for i in range(0, len(number), 7):
        output = output + chr(int(number[i:i + 7], 2)) 
    return output


def BinaryToHexadecimal(number):
    number = createGroups(4, number)
    hex_table = {
          "0000" : '0',
          "0001" : '1',
          "0010" : '2',
          "0011" : '3',
          "0100" : '4',
          "0101" : '5',
          "0110" : '6',
          "0111" : '7',
          "1000" : '8',
          "1001" : '9',
          "1010" : 'A',
          "1011" : 'B',
          "1100" : 'C',
          "1101" : 'D',
          "1110" : 'E',
          "1111" : 'F' 
          }
    output = ""
    for i in number:
        output += hex_table[i]
    return output


def createInputMatrix(plaintext):
    hex_text = ""
    output = []
    
    if len(plaintext)%32:
        plaintext += (32 - len(plaintext)%16)*bogusElement(plaintext)
    plaintexts = createGroups(32, plaintext)
    for plaintext in plaintexts:
        plaintext_matrix = [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0]]
        hex_text = ""
        for i in plaintext:
            hex_text +=  i
        for i in range(4):
            for j in range(4):
                plaintext_matrix[j][i] = hex_text[0:2]
                hex_text = hex_text[2:]
        output.append(plaintext_matrix)
    return output
    
    
def hexadecimalToBinary(word):
    word = word.upper()
    hex_table = {'0' : "0000",
          '1' : "0001",
          '2' : "0010",
          '3' : "0011",
          '4' : "0100",
          '5' : "0101",
          '6' : "0110",
          '7' : "0111",
          '8' : "1000",
          '9' : "1001",
          'A' : "1010",
          'B' : "1011",
          'C' : "1100",
          'D' : "1101",
          'E' : "1110",
          'F' : "1111" }
    
    output = ""
    for i in word:
        output += hex_table[i]
    return output


def stringToHex(word):
    wordToHex = {'A': 'F0', 'B': 'F1', 'C': 'F2', 'D': 'F3', 'E': 'F4', 'F': 'F5', 'G': 'F6', 
                 'H': 'F7', 'I': 'F8', 'J': 'F9', 'K': 'FA', 'L': 'FB', 'M': 'FC', 'N': 'FD', 
                 'O': 'FE', 'P': 'FF', 'Q': 'E0', 'R': 'E1', 'S': 'E2', 'T': 'E3', 'U': 'E4', 
                 'V': 'E5', 'W': 'E6', 'X': 'E7', 'Y': 'E8', 'Z': 'E9', 'a': 'EA', 'b': 'EB', 
                 'c': 'EC', 'd': 'ED', 'e': 'EE', 'f': 'EF', 'g': 'D0', 'h': 'D1', 'i': 'D2', 
                 'j': 'D3', 'k': 'D4', 'l': 'D5', 'm': 'D6', 'n': 'D7', 'o': 'D8', 'p': 'D9', 
                 'q': 'DA', 'r': 'DB', 's': 'DC', 't': 'DD', 'u': 'DE', 'v': 'DF', 'w': 'C0', 
                 'x': 'C1', 'y': 'C2', 'z': 'C3', '.': 'C4', ',': 'C5', '!': 'C6', '@': 'C7', 
                 '#': 'C8', '$': 'C9', '%': 'CA', '^': 'CB', '&': 'CC', '*': 'CD', '(': 'CE', 
                 ')': 'CF', '-': 'B0', '_': 'B1', '+': 'B2', '=': 'B3', '}': 'B4', '{': 'B5', 
                 '[': 'B6', ']': 'B7', ';': 'B8', ':': 'B9', "'": 'BA', '"': 'BB', '?': 'BC', 
                 '/': 'BD', ' ': '00', '1': 'BF', '2': 'A0', '3': 'A1', '4': 'A2', '5': 'A3', 
                 '6': 'A4', '7': 'A5', '8': 'A6', '9': 'A7', '0': 'A8'}
    
    
    output = ""
    for i in word:
        output += wordToHex.get(i)
    return output


def HexToString(word):
    
    HexToWord = {'F0': 'A', 'F1': 'B', 'F2': 'C', 'F3': 'D', 'F4': 'E', 'F5': 'F', 'F6': 'G', 
                 'F7': 'H', 'F8': 'I', 'F9': 'J', 'FA': 'K', 'FB': 'L', 'FC': 'M', 'FD': 'N', 
                 'FE': 'O', 'FF': 'P', 'E0': 'Q', 'E1': 'R', 'E2': 'S', 'E3': 'T', 'E4': 'U', 
                 'E5': 'V', 'E6': 'W', 'E7': 'X', 'E8': 'Y', 'E9': 'Z', 'EA': 'a', 'EB': 'b', 
                 'EC': 'c', 'ED': 'd', 'EE': 'e', 'EF': 'f', 'D0': 'g', 'D1': 'h', 'D2': 'i', 
                 'D3': 'j', 'D4': 'k', 'D5': 'l', 'D6': 'm', 'D7': 'n', 'D8': 'o', 'D9': 'p', 
                 'DA': 'q', 'DB': 'r', 'DC': 's', 'DD': 't', 'DE': 'u', 'DF': 'v', 'C0': 'w', 
                 'C1': 'x', 'C2': 'y', 'C3': 'z', 'C4': '.', 'C5': ',', 'C6': '!', 'C7': '@', 
                 'C8': '#', 'C9': '$', 'CA': '%', 'CB': '^', 'CC': '&', 'CD': '*', 'CE': '(', 
                 'CF': ')', 'B0': '-', 'B1': '_', 'B2': '+', 'B3': '=', 'B4': '}', 'B5': '{', 
                 'B6': '[', 'B7': ']', 'B8': ';', 'B9': ':', 'BA': "'", 'BB': '"', 'BC': '?', 
                 'BD': '/', '00': ' ', 'BF': '1', 'A0': '2', 'A1': '3', 'A2': '4', 'A3': '5', 
                 'A4': '6', 'A5': '7', 'A6': '8', 'A7': '9', 'A8': '0'}
    
    output = ""
    for i in range(0, len(word), 2):
        output += HexToWord.get(word[i] + word[i+1])
    return output
    


def createOutputString(matrix):
    output = ""
    for i in range(4):
        for j in range(4):
            output += matrix[j][i]
    return output
 
    
def xor(a,b):
    a = hexadecimalToBinary(a)
    b = hexadecimalToBinary(b)
    output = ""
    for i in range(len(a)):
        output += str(int(a[i])^int(b[i]))
    return BinaryToHexadecimal(output)


def multiplyHex(a,b):
    return hex(int(a,16) * int(b,16))[2:].upper()


def s_Box(matrix):
    
    s_box = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'], 
         ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'], 
         ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'], 
         ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'], 
         ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'], 
         ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'], 
         ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'], 
         ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'], 
         ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'], 
         ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'], 
         ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'], 
         ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'], 
         ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'], 
         ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'], 
         ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'], 
         ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]
    
    map = {'0': 0, 
         '1': 1, 
         '2': 2, 
         '3': 3, 
         '4': 4, 
         '5': 5, 
         '6': 6, 
         '7': 7, 
         '8': 8, 
         '9': 9, 
         'A': 10, 
         'B': 11, 
         'C': 12, 
         'D': 13, 
         'E': 14, 
         'F': 15}
    try:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = s_box[map[matrix[i][j][0]]][map[matrix[i][j][1]]]
        return matrix
    except:
        for i in range(len(matrix)):
            matrix[i] = s_box[map[matrix[i][0]]][map[matrix[i][1]]]
        return matrix


def inv_s_box(matrix):
    inv_s_box = [['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'], 
             ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'], 
             ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'], 
             ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'], 
             ['72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'], 
             ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84'], 
             ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'], 
             ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'], 
             ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'], 
             ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'], 
             ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'], 
             ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'], 
             ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F'], 
             ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'], 
             ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'], 
             ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']]
    
    map = {'0': 0, 
         '1': 1, 
         '2': 2, 
         '3': 3, 
         '4': 4, 
         '5': 5, 
         '6': 6, 
         '7': 7, 
         '8': 8, 
         '9': 9, 
         'A': 10, 
         'B': 11, 
         'C': 12, 
         'D': 13, 
         'E': 14, 
         'F': 15}

    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = inv_s_box[map[matrix[i][j][0]]][map[matrix[i][j][1]]]
    return matrix


def galois_mult(a, b):
    a = int(a, 16)
    b = int(b, 16)
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1: p ^= a
        hi_bit_set = a & 128
        a <<= 1
        if hi_bit_set == 128: a ^= 27
        b >>= 1
    if len(hex(p % 256)[2:]) == 1:
        return "0" + hex(p % 256)[2:]
    else:
        return hex(p % 256)[2:]


def shiftRows(matrix):
    output = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][(j+i)%len(matrix[i])])
        output.append(row)
    return output


def inv_shiftRows(matrix):
    output = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][(j-i)%len(matrix[i])])
        output.append(row)
    return output


def mixColumns(matrix):
    static = [['02', '03', '01', '01'], 
              ['01', '02', '03', '01'], 
              ['01', '01', '02', '03'], 
              ['03', '01', '01', '02']]
    output = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    
    for i in range(4):
        for j in range(4):
            r = []
            for k in range(4):
                r.append(galois_mult(static[i][k], matrix[k][j]))
            output[i][j] = xor(xor(xor(r[0],r[1]),r[2]),r[3])
    return output


def inv_mixColumns(matrix):
    static = [['0E', '0B', '0D', '09'], 
              ['09', '0E', '0B', '0D'], 
              ['0D', '09', '0E', '0B'], 
              ['0B', '0D', '09', '0E']]
    output = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    
    for i in range(4):
        for j in range(4):
            r = []
            for k in range(4):
                r.append(galois_mult(static[i][k], matrix[k][j]))
            output[i][j] = xor(xor(xor(r[0],r[1]),r[2]),r[3])
    return output


def roundFunction(word, round):
    roundTable = [['01', '00', '00', '00'], 
                  ['02', '00', '00', '00'], 
                  ['04', '00', '00', '00'], 
                  ['08', '00', '00', '00'], 
                  ['10', '00', '00', '00'], 
                  ['20', '00', '00', '00'], 
                  ['40', '00', '00', '00'], 
                  ['80', '00', '00', '00'], 
                  ['1B', '00', '00', '00'], 
                  ['36', '00', '00', '00']]
    word = s_Box([word[1], word[2], word[3], word[0]])
    for i in range(4):
        word[i] = xor(word[i], roundTable[round - 1][i])
    return word


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    output = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        output.append(row)

    return output


def keyExpansion(key):
    words = []
    keys = []
    output = []
    for i in range(4):
        l = []
        for j in range(4):
            l.append(key[0:2])
            key = key[2:]
        words.append(l)
    for i in range(40):
        l = []
        if not len(words)%4:
            l1 = roundFunction(words[-1], int(len(words)/4))
            for j in range(4):
                l.append(xor(words[-4][j], l1[j]))
        else:
            for j in range(4):
                l.append(xor(words[-4][j],words[-1][j]))
        words.append(l)
    for i in range(11):
        keys.append(words[0:4])
        words = words[4:]
    for i in range(len(keys)):
        output.append(transpose(keys[i]))
    return output


def reverse(matrix):
    output = []
    for i in reversed(range(len(matrix))):
        output.append(matrix[i])
    return output


def addRoundKey(matrix, key):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = xor(matrix[i][j], key[i][j])
    return matrix


def createKey(word):
    if len(word)%16:
        word = word + (16 - len(word)%16) * bogusElement(word)
    output = ""
    for i in word:
        output += ''.join(format(ord(i), '08b'))
    return BinaryToHexadecimal(output)


def encryption(plaintext, key):
    plaintext = stringToHex(plaintext)
    plaintexts = createInputMatrix(plaintext)
    keys = keyExpansion(createKey(key))
    ciphertext = ""
    for plaintext in plaintexts:
        state = plaintext
        state = addRoundKey(state, keys[0])
        for i in range(1, 10):
            state = s_Box(state)
            state = shiftRows(state)
            state = mixColumns(state)
            state = addRoundKey(state, keys[i])
        state = s_Box(state)
        state = shiftRows(state)
        state = addRoundKey(state, keys[-1])
        ciphertext += createOutputString(state)
    return ciphertext


def decryption(ciphertext, key):
    ciphertexts = createInputMatrix(ciphertext)
    keys = keyExpansion(createKey(key))
    plaintext = ""
    for ciphertext in ciphertexts:
        state = ciphertext
        state = addRoundKey(state, keys[-1])
        state = inv_shiftRows(state)
        state = inv_s_box(state)
        for i in reversed(range(1,10)):
            state = addRoundKey(state, keys[i])
            state = inv_mixColumns(state)
            state = inv_shiftRows(state)
            state = inv_s_box(state)
        state = addRoundKey(state, keys[0])
        plaintext += createOutputString(state)
    plaintext = HexToString(plaintext)
    return plaintext


# plaintext = input("Enter the text you want to Encrypt: ")
# key = input("Enter the key: ")
# print(f"The encrypted text is: {encryption(plaintext,key)}")
# encrypted_text = input("Enter the encrypted text: ")
# decryption_key = input("Enter the decryption key: ")
# print(f"The decrypted text is: {decryption(encrypted_text,decryption_key)}")