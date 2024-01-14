# crytography.py
import string
KEY = 4


class Cryptography():
    def __init__(self, input):
        self.input = input
        self.characters = string.whitespace + string.punctuation + string.digits + string.ascii_letters
        self.generated_string = ""
        for x in self.characters:
            x = bytes(x,'utf-8')
            x = x[0]+KEY
            self.generated_string += chr(x)

    def encryption(self):
        encryptedString =""
        for x in self.input:
            index = self.characters.index(x)
            encryptedString += self.generated_string[index]
        return encryptedString

    def decryption(self):
        decryptedString = ""
        for x in self.input:
            index = self.generated_string.index(x)
            decryptedString += self.characters[index]
        return decryptedString
