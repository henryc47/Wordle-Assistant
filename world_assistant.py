#author-Henry Chadban
#date-22/01/2022
#The purpose of this program is to solve the wordle game

#our source for english words was compiled by John Lawler of the University of Michigan
#it is available at http://www-personal.umich.edu/~jlawler/wordlist.html

text_list = "/Users/henry_chadban/Documents/Personal Projects, Current/Wordle Assistant/wordlist.txt"

def import_words():
    with open(text_list) as f:
        lines = f.readlines()
    
    culled_lines = []
    for line in lines:
        line = line[0:(len(line)-1)]
        culled_lines.append(line)

    return culled_lines

def wordle_help():
    all_words = import_words()
    #we are only interested in five letter words
    allowed_words = []
    for word in all_words:
        if(len(word))==5:
            allowed_words.append(word)
    
    
    
    num_words_original = len(allowed_words)
    #now enter the main loop where we can add conditions
    while True:
        user_input = input("Please enter the type of rule: ")
        if(user_input=='ban letter') or (user_input=='bl'):
            while True:
                user_input2 = input("Please enter the character to ban: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    new_words = ban_letter(user_input2,allowed_words)
                    break
            allowed_words = new_words
            continue
                        
        elif(user_input=='force letter') or (user_input=='fl'):
            while True:
                user_input2 = input("Please enter the character to force: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    new_words = force_letter(user_input2,allowed_words)
                    break
                        
            allowed_words = new_words
            continue
        
        elif(user_input=='force letter position') or (user_input=='flp'):
            while True:
                user_input2 = input("Please enter the character to force position: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    while True:
                        user_input3 = int(input("Please enter the position to force: "))
                        if (user_input3>5) or (user_input3<1):
                            print("position must be between 1 and 5 inclusive")
                            continue
                        else:
                            new_words = force_letter_position(user_input2,user_input3,allowed_words)        
                            break     
                    break
            allowed_words = new_words
            continue
        
        elif(user_input=='ban letter position') or (user_input=='blp'):
            while True:
                user_input2 = input("Please enter the character to ban position: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    while True:
                        user_input3 = int(input("Please enter the position to ban: "))
                        if (user_input3>5) or (user_input3<1):
                            print("position must be between 1 and 5 inclusive")
                            continue
                        else:
                            new_words = ban_letter_position(user_input2,user_input3,allowed_words)        
                            break     
                    break       
            allowed_words = new_words
            continue
        
        elif (user_input=='ban multiple letter') or (user_input=='bml'):
            while True:
                user_input2 = input("Please enter the character to ban multiple copies of: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    user_input3 = int(input("maximum number of copies of character: "))
                    new_words = ban_multiple_letters(user_input2,user_input3,allowed_words)
                    break
        
            allowed_words = new_words
            continue
        
        elif(user_input=="valid words") or (user_input=="vw"):
            print(allowed_words)
            num_words = len(allowed_words)
            print("number of words allowed now ", num_words, " out of ", num_words_original, " five letter words")
        
        elif(user_input=="end"):
            return 0
        
        else:
            print("please enter valid input")
            continue
            
def ban_letter(letter,allowed_words):
    new_words = []
    for word in allowed_words:
        letter_in_word = False
        for i in word:
            if(i==letter):
                letter_in_word = True
        if letter_in_word == False:
            new_words.append(word)
    return new_words          

def force_letter(letter,allowed_words):
    new_words = []
    for word in allowed_words:
        letter_in_word = False
        for i in word:
            if(i==letter):
                letter_in_word = True
        if letter_in_word == True:
            new_words.append(word)
    return new_words

def force_letter_position(letter,position,allowed_words):
    new_words = []
    position = position-1#convert to standard programming position notation, with 0 as first entry
    for word in allowed_words:
        position_character = word[position]
        if(position_character==letter):
            new_words.append(word)
        else:
            continue
    return new_words                                                         

def ban_letter_position(letter,position,allowed_words):
    new_words = []
    position = position-1#convert to standard programming position notation, with 0 as first entry
    for word in allowed_words:
        position_character = word[position]
        if(position_character==letter):
            continue
        else:
            new_words.append(word)
            continue
            
    return new_words                 
        
def ban_multiple_letters(letter,max_num,allowed_words):
    new_words = []
    for word in allowed_words:
        char_count = 0#count of the character we are checking in the word
        for i in word:
            if i==letter:
                char_count = char_count + 1
                continue
            else:
                continue
        if char_count>max_num:
            continue
        else:
            new_words.append(word)
            continue
        
    return new_words
                

        

