import re
from random import shuffle


class Hangman():

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions','just','trust','pedagogy']
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        guess = input( "Enter a letter : " )
        its_letter = re.search( r"[a-z]|[A-Z]", guess )
        num_letter = len( guess )
        if its_letter != None and num_letter == 1:
            if guess in self.word_to_find:
                right_letter = [index for index, letter in enumerate( self.word_to_find ) if letter == guess]
                for index in right_letter:
                    self.correctly_guessed_letters[index] = guess.upper()
                    self.turn_count += 1
            # COACHES' NOTE: Subdividing into a few more functions could have avoided this 'floating' else statement. Hard to follow the logic this way.
            else:
                self.wrongly_guessed_letters.append( guess )
                self.error_count += 1
                self.lives -= 1
                self.turn_count += 1
        # COACHES' NOTE: This else statement is not needed if you return out of the function in your if statement.
        else:
            print( "Only one letter and/or only letter" )
            self.play()

    def start_game(self):
        shuffle( self.possible_words )
        self.word_to_find = list( self.possible_words[1] )
        num_letter = len( self.word_to_find )
        self.correctly_guessed_letters = list( num_letter * '_' )
        # COACHES' NOTE: 1 -> True
        while 1:
            self.play()
            print( self.correctly_guessed_letters )
            print( self.wrongly_guessed_letters )
            if self.word_to_find == self.correctly_guessed_letters:
                self.well_played()
                break
            if self.lives == 0:
                self.game_over()
                break

    def game_over(self):
        print( "GAME OVER" )

    def well_played(self):
        print( f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!" )

# COACHES' NOTE: Good job overall, nice implementation of OOP concepts.
