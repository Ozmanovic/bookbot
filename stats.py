def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def count_chars(text):
    chardic = {


    }

    for char in text:
        lower_char = char.lower()
        if lower_char in chardic:
            chardic[lower_char] += 1
        else:
            chardic[lower_char] = 1
    return chardic    

def sortti(dictie):
    
    new_dict = []
    

    
    for char in dictie:
        

        if char.isalpha():
            
            char_dict = {"char":char, "count": dictie[char]}
            new_dict.append(char_dict)
            
        else:
            continue
    def sort_on(dictie):
        return dictie["count"]    
    
    new_dict.sort(reverse=True, key=sort_on)
    
    return new_dict