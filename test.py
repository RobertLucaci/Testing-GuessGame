import unittest
import guessgame

class GuessGame(unittest.TestCase):
    def test_input(self):
        result = guessgame.guess_game(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = guessgame.guess_game(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guessgame.guess_game(5, 25)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guessgame.guess_game(5, '25')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
