from code.FizzBuzz import it_FizzorBuzz

import unittest

class testFizzorBuzz(unittest.TestCase):
    def test_give_3(self):
        number = 3
        it_Fizz = it_FizzorBuzz(number)
        self.assertEqual(it_Fizz,"Fizz")
    
    def test_give_5(self):
        number = 5
        it_Buzz = it_FizzorBuzz(number)
        self.assertEqual(it_Buzz,"Buzz")    

    def test_give_15(self):
        number = 15
        it_Fizz = it_FizzorBuzz(number)
        self.assertEqual(it_Fizz,"FizzBuzz")
    
    def test_give_20(self):
        number = 20
        it_Fizz = it_FizzorBuzz(number)
        self.assertEqual(it_Fizz,"Buzz")

    def test_give_negative1(self):
        number = -1
        it_Fizz = it_FizzorBuzz(number)
        self.assertEqual(it_Fizz,"outofrange") 
    
    def test_give_1001(self):
        number = 1001
        it_Fizz = it_FizzorBuzz(number)
        self.assertEqual(it_Fizz,"outofrange") 