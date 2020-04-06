#!/usr/bin/env python3

from random import choice

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, last_move):
        pass


class HumanPlayer(Player):
    def move(self):
        myChoice = input("choose a move (paper, scissors, rock): ").lower()
        while myChoice not in moves:
            print("Not a valid move!")
            return self.move()
        return myChoice


class RandomPlayer(Player):
    def move(self):
        return choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def learn(self, last_move):
        self.last_move = last_move

    def move(self):
        if (self.last_move is None):
            return Player.move(self)
        return self.last_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def move(self):
        if (self.last_move is None):
            move = Player.move(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if (beats(move1, move2) is True):
            print("PLAYER WINS :)")
            self.score1 += 1
        elif (move1 == move2):
            print("It's a DRAW")
            pass
        else:
            print("COMPUTER WINS")
            self.score2 += 1

        print(f"Player Move: {move1}, Computer Move: {move2}")
        print(f"Player Score: {self.score1}, Computer Score: {self.score2}")
        
        self.p1.learn(move1)
        self.p2.learn(move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
        if (self.score1 > self.score2):
            print("PLAYER is the WINNER :)")
        elif (self.score1 == self.score2):
            print("No one is the Winner")
        else:
            print("COMPUTER is the WINNER")
        print("Game over!")


if __name__ == '__main__':
    Player1 = HumanPlayer()
    Player2 = ReflectPlayer()
    game = Game(Player1, Player2)
    game.play_game()
