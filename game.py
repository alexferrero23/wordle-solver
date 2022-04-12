import random
from termcolor import colored

def read_words(length: int) -> list:
    '''       
    Reads the file containing all words from RAE dictionary
    
    Parameters
    ----------        
    length : integer
             Used to filter by teh length of the words    
             
    Returns 
    -------
    game_list : list
                Game list of words to play with
    '''
    
    with open('data/words_rae.txt') as file:
        lines = [line.rstrip() for line in file]
    game_list = []
    [game_list.append(word) for word in lines if len(word)==length]
    return game_list

def clean_words(game_list: list) -> list:
    '''       
    Cleans game list to delete accents and remove possible duplicates
    
    Parameters
    ----------        
    game_list : list
             Game list of words to play with    
             
    Returns 
    -------
    game_list : list
                Game list of words to play with
    '''    
    
    game_list = [word.replace("á", "a") for word in game_list]
    game_list = [word.replace("é", "e") for word in game_list]
    game_list = [word.replace("í", "i") for word in game_list]
    game_list = [word.replace("ó", "o") for word in game_list]
    game_list = [word.replace("ú", "u") for word in game_list]
    
    game_list = list(dict.fromkeys(game_list))
    
    #random.shuffle(game_list)
    
    return game_list

def play_game(game_list: list, number_attempts: int):
    
    random.shuffle(game_list)
    word_game = game_list[0]
    ################## TEST
    #word_game = 'aonio'
    #################
    word_game_split = list(word_game)
    
    for attempt in range(number_attempts):
        
        #pending make sure this is true
        while True:
            user_word = input(f'\n Introduce una palabra con {len(word_game)} letras: ')
            if user_word not in game_list and len(user_word) == len(word_game):
                print(colored('Esta palabra no esta en el diccionario', 'red'))
                continue
            elif len(user_word) != len(word_game):
                print(colored(f'Esta palabra tiene un numero de letras distinto de {len(word_game)}', 'red'))
                continue
            else:
                break
            
        user_word_split = list(user_word)
        
        output = iteration_output(word_game_split, user_word_split)
        
        print(user_word)
        for i in output:
            if i == 'green':
                print(colored('0', 'green'), end='')
            elif i == 'yellow':
                print(colored('0', 'yellow'), end='')
            elif i == 'red':
                print(colored('0', 'red'), end='')

        if word_game_split == user_word_split:
            print(colored(f'\n Enhorabuena, palabra adivinada en {attempt+1} intentos', 'green'))
            break
            
    if word_game_split != user_word_split:
        print(f'\n 1lucky, la palabra era {word_game}')

    
    

def iteration_output(word_game_split: list, user_word_split: list) -> list:
    '''
    pending
    '''
    output = []
    for i, letter in enumerate(user_word_split):
        #green
        if letter in word_game_split and user_word_split[i] == word_game_split[i]:
            output.append('green')
        #yellow
        elif letter in word_game_split and user_word_split[i] != word_game_split[i]:
            output.append('yellow')
        #red
        elif letter not in word_game_split:
            output.append('red')
            
    return output
        
        

    



    
if __name__ == '__main__':
    game_list = read_words(5)
    game_list = clean_words(game_list)
    #print(iteration_output('aonio','arpia'))
    play_game(game_list, 6)
