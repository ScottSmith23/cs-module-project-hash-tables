

def word_count(s):
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

    return cache






if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))