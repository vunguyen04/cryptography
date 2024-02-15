'''
SHA-1 algorithm class
+Design by Vu Nguyen
+Credit to:
    https://en.wikipedia.org/wiki/SHA-1
    https://www.youtube.com/watch?v=kmHojGMUn0Q
+Example used of the algorithm is at the last of the page
'''

class SHA1():
    def __init__(self):
        pass


    #string to ascii is store string in array of ASCII number
    #return array of string
    def string_to_ascii(self, input):
        result = []
        for i in range(len(input)):
            result.append(ord(input[i]))
        return result


    #dec_to_binary is used to convert array of decimal to binary
    #return array of string
    def dec_to_binary(self, input):
        result = []
        temp = ""
        for i in input:
            while i != 0:
                temp = str((i % 2)) + temp
                i = int(i/2)
            result.append(temp)
            temp = ""
        return result


    #binary_to_hex is used to convert string of binary to string of hex
    def binary_to_hex(self, input):
        result = ""
        while len(input) % 4 != 0:
            input = "0"+input
        for i in range(0, len(input), 4):
            temp = input[i:i+4]
            if temp == "0000":
                result += "0"
            elif temp == "0001":
                result += "1"
            elif temp == "0010":
                result += "2"
            elif temp == "0011":
                result += "3"
            elif temp == "0100":
                result += "4"
            elif temp == "0101":
                result += "5"
            elif temp == "0110":
                result += "6"
            elif temp == "0111":
                result += "7"
            elif temp == "1000":
                result += "8"
            elif temp == "1001":
                result += "9"
            elif temp == "1010":
                result += "A"
            elif temp == "1011":
                result += "B"
            elif temp == "1100":
                result += "C"
            elif temp == "1101":
                result += "D"
            elif temp == "1110":
                result += "E"
            elif temp == "1111":
                result += "F"
        return result


    #binary_left_rotate is used to shift bit of binary number to left circularly
    #return string
    def binary_left_rotate(self, input, n_shift):
        result = input[n_shift:] + input[:n_shift]
        return result


    #xor_bitwise is used to return string of A XOR B in binary
    def xor_bitwise(self, inputA, inputB):
        result = ""
        for i in range(len(inputA)):
            if inputA[i] == "0":
                if inputB[i] == "0":
                    result += "0"
                else:
                    result += "1"
            else:
                if inputB[i] == "0":
                    result += "1"
                else:
                    result += "0"
        return result


    #and_bitwise is used to return string of A AND B in binary
    def and_bitwise(self, inputA, inputB):
        result = ""
        for i in range(len(inputA)):
            if inputA[i] == "1" and inputB[i] == "1":
                result += "1"
            else:
                result += "0"
        return result


    #or_bitwise is used to return string of A OR B in binary
    def or_bitwise(self, inputA, inputB):
        result = ""
        for i in range(len(inputA)):
            if inputA[i] == "0" and inputB[i] == "0":
                result += "0"
            else:
                result += "1"
        return result


    #not_bitwise is used to return a string of not A in binary
    def not_bitwise(self, input):
        result = ""
        for i in range(len(input)):
            if input[i] == "0":
                result += "1"
            else:
                result += "0"
        return result


    #binary_addition is used to add two binary numbers
    def binary_addition(self, inputA, inputB):
        result = ""
        remind = 0
        while len(inputA) > len(inputB):
            inputB = "0" + inputB
        while len(inputB) > len((inputA)):
            inputA = "0" + inputA

        for i in range(len(inputA)-1, -1, -1):
            if int(inputA[i]) + int(inputB[i]) + remind == 0:
                result = "0" + result
                remind = 0
            elif int(inputA[i]) + int(inputB[i]) + remind == 1:
                result = "1" + result
                remind = 0
            elif int(inputA[i]) + int(inputB[i]) + remind == 2:
                result = "0" + result
                remind = 1
            elif int(inputA[i]) + int(inputB[i]) + remind == 3:
                result = "1" + result
                remind = 1
        if remind == 1:
            result = "1" + result
            remind = 0
        return result


    #truncate function is truncate front excess bit
    def truncate(self, input, length):
        result = input[len(input)-length:]
        return result


    def sha1_algorithm(self, input):
        #initialize value for SHA1
        h0 = "01100111010001010010001100000001"
        h1 = "11101111110011011010101110001001"
        h2 = "10011000101110101101110011111110"
        h3 = "00010000001100100101010001110110"
        h4 = "11000011110100101110000111110000"

        #Step 1: take input and split it into array of ASCII Code
        array_ascii = self.string_to_ascii(input)

        #Step 2: Convert ASCII array to binary array
        array_binary = self.dec_to_binary(array_ascii)

        #Step 3: create a 8-bit binary for each number in array_binary by add 0 to front of the number
        #Step 4: join all number in array_binary and add 1 to the end
        binary_characters = ""
        len_array_binary_in_dec = 0

        for i in range(len(array_binary)):
            while len(array_binary[i]) % 8 != 0:
                array_binary[i] = "0" +array_binary[i]
            binary_characters += array_binary[i]
            len_array_binary_in_dec += len(array_binary[i])
        binary_characters += "1"

        #Step 5: create binary message with zero until its length is 512 mod 448
        while len(binary_characters) % 512 != 448:
            binary_characters += "0"

        #Step 6: define a length of all bit in array_binary and turn it into binary number
        temp_len_in_dec = [len_array_binary_in_dec]
        len_array_binary_in_bit = self.dec_to_binary(temp_len_in_dec)

        #Step 7: add 0 to front of len_array_binary_in_bit until length in binary is 64 bit
        while len(len_array_binary_in_bit[0]) != 64:
            len_array_binary_in_bit[0] = "0" + len_array_binary_in_bit[0]

        #Step 8: append len_array_binary_in_bit to binary message in step 5
        binary_characters += len_array_binary_in_bit[0]

        #Step 9: split the message into array_binary_512characters of 512 characters
        array_binary_512characters = []
        for i in range(0, len(binary_characters), 512):
            array_binary_512characters.append(binary_characters[i:i+512])

        #Step10: split each 512 characters of array_binary_512characters into subarray array_binary_32bit of sixteen 32-bit 'words'
        array_binary_32bit = []
        temp_arr = []
        for i in range(len(array_binary_512characters)):
            for j in range(0, 512, 32):
                temp_arr.append(array_binary_512characters[i][j:j+32])
            array_binary_32bit.append(temp_arr)
            temp_arr = []

        #Step 11: Loop through array_binary_32bit and extend each array to 80 'words' using bitwise operation
        for j in range(0, len(array_binary_32bit)):
            for i in range(16, 80, 1):
                wordA = array_binary_32bit[j][i-3]
                wordB = array_binary_32bit[j][i - 8]
                wordC = array_binary_32bit[j][i - 14]
                wordD = array_binary_32bit[j][i - 16]

                xorA = self.xor_bitwise(wordA, wordB)
                xorB = self.xor_bitwise(xorA, wordC)
                xorC = self.xor_bitwise(xorB, wordD)

                newWord = self.binary_left_rotate(xorC, 1)
                array_binary_32bit[j].append(newWord)

        #main loop: loop through each array_binary_32bit to continuously create a new words
        for i in range(len(array_binary_32bit)):
            # Initialize some variables for each 80 "word" array
            a = h0
            b = h1
            c = h2
            d = h3
            e = h4
            for j in range(len(array_binary_32bit[i])):
                #if else to find f and k depending on spot of word
                if j < 20:
                    b_and_c = self.and_bitwise(b, c)
                    not_b = self.not_bitwise(b)
                    not_b_and_d = self.and_bitwise(not_b, d)
                    f = self.or_bitwise(b_and_c, not_b_and_d)
                    k = "01011010100000100111100110011001"
                elif j < 40:
                    b_xor_c = self.xor_bitwise(b, c)
                    f = self.xor_bitwise(b_xor_c, d)
                    k = "01101110110110011110101110100001"
                elif j < 60:
                    b_and_c = self.and_bitwise(b, c)
                    b_and_d = self.and_bitwise(b, d)
                    c_and_d = self.and_bitwise(c, d)
                    bc_or_bd = self.or_bitwise(b_and_c, b_and_d)
                    f = self.or_bitwise(bc_or_bd, c_and_d)
                    k = "10001111000110111011110011011100"
                else:
                    b_xor_c = self.xor_bitwise(b, c)
                    f = self.xor_bitwise(b_xor_c, d)
                    k = "11001010011000101100000111010110"
                #temp_add = (a left rotate 5) + f + e + k + w[i]
                temp_add = self.binary_addition(self.binary_left_rotate(a, 5), f)
                temp_add = self.binary_addition(temp_add, e)
                temp_add = self.binary_addition(temp_add, k)
                temp_add = self.binary_addition(temp_add, array_binary_32bit[i][j])
                temp_add = self.truncate(temp_add, 32)
                #swap around
                e = d
                d = c
                c = self.binary_left_rotate(b, 30)
                b = a
                a = temp_add

            # Step 14: add initialized variables 'h_n' with new coressponding words
            h0 = self.truncate(self.binary_addition(h0, a), 32)
            h1 = self.truncate(self.binary_addition(h1, b), 32)
            h2 = self.truncate(self.binary_addition(h2, c), 32)
            h3 = self.truncate(self.binary_addition(h3, d), 32)
            h4 = self.truncate(self.binary_addition(h4, e), 32)

        #Step 15: join every h_n and convert from binary to hex
        result = self.binary_to_hex(h0 + h1 + h2 + h3 + h4)
        return result
