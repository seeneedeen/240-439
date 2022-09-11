from catAndmouse import catAndMouse

import unittest

class testcatAnamouse(unittest.TestCase):
    def test_return_catB(self):
        result = catAndMouse(1,5,4)
        self.assertEqual(result,"Cat B")

    def test_return_catA(self):
        result = catAndMouse(1,2,1)
        self.assertEqual(result,"Cat A")
    
    def test_return_mouseC(self):
        result = catAndMouse(1,3,2)
        self.assertEqual(result,"Mouse C")