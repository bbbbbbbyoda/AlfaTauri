# # 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты,
# а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

from random import shuffle
from random import choice

rank = ['A', 'К', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
mastb = ["червы", "бубны", "трефы", "пики"]


class Card:

    def __init__(self, mastb, rank):
        self.mastb = mastb
        self.rank = rank

    def info_rank(self):
        return self.rank

    def __str__(self):
        return f'{self.rank} {self.mastb}'


class Deck:

    def __init__(self, cards):
        self.cards = cards

    def deck_info(self):
        for card in self.cards:
            print(card)

    def mix_card(self):
        shuffle(self.cards)

    def one_card(self):
        del_card = choice(self.cards)
        return del_card


cards = [Card(m, r) for m in mastb for r in rank]

deck = Deck(cards)
print('Целая колода: ')
deck.deck_info()
deck.mix_card()
print('Перемешанная колода: ')
deck.deck_info()
print('Выдача одной карты: ')
print(deck.one_card())
