import unittest
import main
import question_model


class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main.Question("Who owns Tesla Company?", "B"))


if __name__ == '__main__':
    unittest.main()
