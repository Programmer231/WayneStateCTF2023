from os import urandom
from Crypto.Cipher import AES
import secretMessage

assert all([x.isupper() or x in '{_} ' for x in secretMessage])


class Cipher:

    def __init__(self):
        key = urandom(16)
        self.salt = urandom(15)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


def main():
    cipher = Cipher()
    encrypted = cipher.encrypt(secretMessage)
    encrypted = "\n".join([c.hex() for c in encrypted])

    with open('output.txt', 'w+') as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()
