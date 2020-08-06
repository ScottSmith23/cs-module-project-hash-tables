def no_dups(s):
    # Your code here

    if s == "":
        return ""
    cache = {}    
    for word in s.split():
        if word not in cache:
           cache[word] = word
    
    words=list(cache.values())
        
    return " ".join(words)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))