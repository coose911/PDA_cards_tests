import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    
    def setUp(self):
        self.card = Card("clubs", 10)
        self.card1 = Card("spades", 1)
        self.cards = [self.card, self.card1]
        

    def test_check_for_ace(self):
        card_game = CardGame()
        self.assertEqual(False, card_game.check_for_ace(self.card))

    
    def test_highest_card(self):
        card_game = CardGame()
        highest_card = card_game.highest_card(self.card, self.card1)
        self.assertEqual(self.card , highest_card)

    
    def test_cards_total(self):
        card_game = CardGame()
        self.assertEqual("You have a total of 10", card_game.cards_total(self.cards))