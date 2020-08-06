# Your code here

# Read in all the words in one go
with open("applications/histo/robin.txt") as f:
    s = f.read()

def histogram(s):
    # Your code here
    cache = {}

    #remove specific characters
    for char in '":;,.-+=/\\|[]{}()*^&':  
        s = s.replace(char,'')
    #if no input return empty dict
    if s == "":
        return {}
        
    for word in s.split():
        lowcase = word.lower()
        if lowcase not in cache:
            cache[lowcase] = 1
        else:
            cache[lowcase] += 1
    
    sorter = sorted(cache.items(),key = lambda pair: pair[1], reverse = True)

    for key, value in sorter:

        string1 = (key)
        string2 = ("#" * value)

        print( '{:<20s} {:<10s}'.format(string1, string2) )
        


histogram(s)