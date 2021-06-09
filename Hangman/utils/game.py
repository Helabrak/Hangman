import random

class Hangman:
    def __init__(self, word):
        self.word = word
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'just', 'trust', 'pedagogy']
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters=[]
        self.wrongly_guessed_letters = []
        self.turn_count=[0]
        self.error_count=[0]


    def play (self):
        letter=input('please enter a letter')
        if letter in self.word_to_find:
            for index, l in enumerate(self.word_to_find):
                if l ==letter:
                    self.correctly_guessed_letters[index]=letter
            print(self.correctly_guessed_letters)
            self.turn_count+=1
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
            self.turn_count += 1

    def start_game(self):
        word = random.choice(self.possible_words)
        self.word_to_find=list(word)
        while True:
            self.play()
            if self.lives ==0:
                self.game_over()
                break
            if self.word_to_find ==self.correctly_guessed_letters:
                self.well_played()
                break

    def game_over(self):
        print("Gameover")

    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")


