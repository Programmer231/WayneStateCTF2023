enc_flag = ""
flag = ""
import key

#key is 1 ASCII character
assert(len(chr(key)) == 1)

for each in flag:
    each = chr(ord(each) ^ key)
    enc_flag += each

with open("flag.enc.txt", "w") as outfile:
    outfile.write(enc_flag)
    print(enc_flag)