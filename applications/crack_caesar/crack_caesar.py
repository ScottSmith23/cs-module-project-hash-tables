# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# Read in all the words in one go
with open("applications/crack_caesar/ciphertext.txt") as f:
    s = f.read()

def ciphercrack(s):
    # Your code here
    freq = {}
    cipher = ['E','T','A','O','H','N','R','I','S','D','L','W','U','G','F','B','M','Y','C','P','K','V','Q','J','X','Z',""]

    #if no input return empty dict
    if s == "":
        return {}

    #adds and counts only letters to a dict
    for char in s:
        if char.isalpha():
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

    #sorts the dict in descending order
    sorter = sorted(freq.items(),key = lambda pair: pair[1], reverse = True)

    #adds the corresponding letter from the cipher to the dict
    counter = 0
    decoded = dict(sorter)
    for key,value in decoded.items():
        decoded[key] = cipher[counter]
        counter +=1

    #decodes and prints the input
    string = ""
    for word in s:
        if word in decoded:
            string += decoded[word]
        else:
            string += word
    return string


decrypt = ciphercrack(s)

with open("applications/crack_caesar/decryptedtext.txt", "w") as file:
    file.write(decrypt)