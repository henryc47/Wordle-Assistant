#author-Henry Chadban
#date-22/01/2022
#The purpose of this program is to solve the wordle game
#Our source for wordle words was taken directly from the games source code by
#Tab Atkins Jr in 2021, https://github.com/tabatkins/wordle-list/blob/main/words


import numpy as np#for the argsort
import random

text_list = "/Users/henry_chadban/Documents/Personal Projects, Current/Wordle Assistant/wordlist2.txt"

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
    
    allowed_words = ban_letter('-',allowed_words)
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
                    allowed_words = ban_letter(user_input2,allowed_words)
                    break
            continue
                        
        elif(user_input=='force letter') or (user_input=='fl'):
            while True:
                user_input2 = input("Please enter the character to force: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    allowed_words = force_letter(user_input2,allowed_words)
                    break
                        
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
                            allowed_words = force_letter_position(user_input2,user_input3,allowed_words)        
                            break     
                    break
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
                            allowed_words = ban_letter_position(user_input2,user_input3,allowed_words)        
                            break     
                    break       
            continue
        
        elif (user_input=='ban multiple letter') or (user_input=='bml'):
            while True:
                user_input2 = input("Please enter the character to ban multiple copies of: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    user_input3 = int(input("maximum number of copies of character: "))
                    allowed_words = ban_multiple_letters(user_input2,user_input3,allowed_words)
                    break
        
            continue
        
        elif(user_input=="valid words") or (user_input=="vw"):
            print(allowed_words)
            num_words = len(allowed_words)
            print("number of words allowed now ", num_words, " out of ", num_words_original, " five letter words")
        
        elif(user_input=="get letter frequencies") or (user_input=='glf'):
            letter_frequencies = get_letter_frequency(allowed_words)
            for i in range(26):#go through all the letters in the alphabet
                print(chr(i+97),letter_frequencies[i])
                
        elif(user_input=="get position frequencies") or (user_input=='gpf'):
            position_frequencies =  get_letter_position_frequency(allowed_words)
            for i in range(26):#go through all the letters in the alphabet
                print(chr(i+97),end=' ')
                for j in range(5):#go through all the characters in each five letter word
                    letter_position = i*5 + j
                    position_frequency = position_frequencies[letter_position]
                    print(position_frequency,end=' ')
                print('')
        
        elif(user_input=='word value') or (user_input=='wv'):
            word_values = word_value(allowed_words)
            for i in range(len(allowed_words)):
                print(allowed_words[i],' ',word_values[i])
            continue
        
        elif(user_input=='best words' or (user_input=='bw')):
            user_input2 =  int(input("how many words do you want to print: "))
            best_n_words(user_input2,allowed_words)
            continue
        
        elif(user_input=='worst words') or (user_input=='ww'):
            user_input2 =  int(input("how many words do you want to print: "))
            worst_n_words(user_input2,allowed_words)
            continue
        
        elif(user_input=='random word') or (user_input=='rw'):
            num_words = len(allowed_words)
            random_word_position = random.randint(0,num_words-1)
            print(allowed_words[random_word_position])
            continue
        
        elif(user_input=="force letter ban position") or (user_input=='flbp'):
            while True:
                user_input2 = input("Please enter the character to force: ")
                if len(user_input2)!=1:
                    print("please enter a single character")
                    continue
                else:
                    while True:
                        user_input3 = int(input("Please enter the position where you wish to ban that character: "))
                        if (user_input3>5) or (user_input3<1):
                            print("position must be between 1 and 5 inclusive")
                            continue
                        else:
                            allowed_words = force_letter(user_input2,allowed_words)
                            allowed_words = ban_letter_position(user_input2,user_input3,allowed_words)        
                            break 
                    break
            continue
            
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

#gets the frequency of letters in the list of allowed words
def get_letter_frequency(allowed_words):
    letter_frequencies = [0]*26
    #letter frequencies stored as a length 26 list
    for word in allowed_words:
        for i in word:
            letter_value = ord(i)-97
            if (letter_value>=0) and (letter_value<=26):
                letter_frequencies[letter_value] = letter_frequencies[letter_value]+1
            else:
                continue

    return letter_frequencies         
                
def get_letter_position_frequency(allowed_words):
    letter_position_frequencies = [0]*26*5
    #array position is determined by letter position in alphabet times five + position in word starting at zero
    for word in allowed_words:
        for i in range(5):
            letter = word[i]
            letter_value = ord(letter)-97
            if (letter_value>=0) and (letter_value<=26):
                total_value  = (letter_value*5)+i
                letter_position_frequencies[total_value] = letter_position_frequencies[total_value]+1
            else:
                continue
            
    return letter_position_frequencies          

def word_value(allowed_words):
    letter_frequency = get_letter_frequency(allowed_words)
    position_frequency = get_letter_position_frequency(allowed_words)
    num_words = len(allowed_words)
    word_value_array = [0]*num_words#array to store the value of every word
    for i in range(num_words):
        word = allowed_words[i]
        letter_in_word = [0]*26#is a letter in the word
        for j in range(5):#go through all the characters in a word
            letter = word[j]
            letter_value = ord(letter)-97#value of the letter where a=0,b=1,etc
            if(letter_value>=0) and (letter_value<=26):#make sure it is a valid lower case letter
                letter_position_value = letter_value*5+j
                #add the letter position frequency to the word value
                word_value_array[i] = word_value_array[i]+position_frequency[letter_position_value]
                #we know the letter is now in the word
                letter_in_word[letter_value]=1
            else:
                continue
        #add the overall frequency of all the letters found in the word to the word value
        #we only do not double count letters found in a word more than once
        value_from_letters = 0
        for k in range(26):
            value_from_letters = value_from_letters + letter_frequency[k]*letter_in_word[k]
        
        word_value_array[i] = word_value_array[i]+value_from_letters
        
    return word_value_array        
                      
def best_words(allowed_words):
    word_values = word_value(allowed_words)
    word_values = np.array(word_values)
    word_ranks = word_values.argsort()
    word_ranks = word_ranks[::-1]#reverse the array so largest values are at the left side
    return (word_ranks,word_values)

def best_n_words(n,allowed_words):
    (word_ranks,word_values) = best_words(allowed_words)
    number_words = len(allowed_words)
    for i in range(min(n,number_words)):
        print(i, ' ', allowed_words[word_ranks[i]],' ',word_values[word_ranks[i]])
    return

def worst_n_words(n,allowed_words):
    (word_ranks,word_values) = best_words(allowed_words)
    number_words = len(allowed_words)
    for i in range(min(n,number_words)):
        print(number_words-i-1, ' ', allowed_words[word_ranks[number_words-i-1]],' ',word_values[word_ranks[number_words-i-1]])
    return        
