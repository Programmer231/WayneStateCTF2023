def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}

    #alphabet for replacing hashes with random letters
    alphabet = 	['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '?', '{', '}', '.', '_', '1']

    #counter for moving through the alphabet
    counter = 0

    #for loop to count number of occurances of a hash
    for item in my_list:
        if (item in freq.keys()):
            freq[item] +=1
        else:
            freq[item] = 1
    
    #print # of occurances for hash
    for key, value in freq.items():
        print(f'{key}, {value}')


    #reset dictionary
    freq = {}   

    #If hash = c3a63e66d719a3b8f855e92802d45fca, replace it with a space, otherwise assign it a random letter
    for item in my_list:
        if(item == "c3a63e66d719a3b8f855e92802d45fca"):
            freq[item] = " "
        if (item not in freq.keys()):
            freq[item] = alphabet[counter]
            counter += 1
    

    list_of_strings = [str(freq[x]) for x in my_list]

    return list_of_strings


def FrequencyAnalysis():
    with open("output.txt", "r") as f:
        x = f.read()
    x = x.split("\n")
    strings = CountFrequency(x)
    print("".join(strings))
    

 
 
# Driver function
if __name__ == "__main__":
    FrequencyAnalysis()