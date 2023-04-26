with open("flag.enc.txt", "r") as infile:
    flag = infile.read()

for i in range(256):
    test = ""
    for each in flag:
        each = chr(ord(each) ^ i)
        test += each
    try:
        print(test + '\n')
    except:
        continue