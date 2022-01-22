#author-Henry Chadban
#date-22/01/2022
#The purpose of this program is to solve the wordle game
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
        if(user_input=='ban letter'):
            while True:
                user_input2 = input("Please enter the character to ban: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    new_words = []
                    for word in allowed_words:
                        letter_in_word = False
                        for i in word:
                            if(i==user_input2):
                                letter_in_word = True
                        if letter_in_word == False:
                            new_words.append(word)
                    break
            allowed_words = new_words
            continue
                        
        elif(user_input=='force letter'):
            while True:
                user_input2 = input("Please enter the character to force: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    new_words = []
                    for word in allowed_words:
                        letter_in_word = False
                        for i in word:
                            if(i==user_input2):
                                letter_in_word = True
                        if letter_in_word == True:
                            new_words.append(word)
                    break
                        
            allowed_words = new_words
            continue
        
        elif(user_input=='force letter position'):
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
                            user_input3 = user_input3-1#convert to standard programming position notation, with 0 as first entry
                            new_words = []
                            for word in allowed_words:
                                position_character = word[user_input3]
                                if(position_character==user_input2):
                                    new_words.append(word)
                            break
                    break       
            allowed_words = new_words
            continue
        
        elif(user_input=='ban letter position'):
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
                            user_input3 = user_input3-1#convert to standard programming position notation, with 0 as first entry
                            new_words = []
                            for word in allowed_words:
                                position_character = word[user_input3]
                                if(position_character!=user_input2):
                                    new_words.append(word)
                            break
                    break       
            allowed_words = new_words
            continue
        
        elif(user_input=="valid words"):
            print(allowed_words)
            num_words = len(allowed_words)
            print("number of words allowed now ", num_words, " out of ", num_words_original, " five letter words")
        
        elif(user_input=="end"):
            return 0
        
        else:
            print("please enter valid input")
            continue
            
            
                                                    
                
                
        
                            

        

