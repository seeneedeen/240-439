from code.FizzBuzz import it_FizzorBuzz

import unittest

class testFizzorBuzz(unittest.TestCase):
    def test_give_3(self):
        number = 3
        it_Fizz = it_FizzorBuzz(number)
        self.assertEqual(it_Fizz,"Fizz")