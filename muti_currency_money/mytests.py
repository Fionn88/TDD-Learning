import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):
      def test_hello(self):
        self.assertEqual(times(2), 10)

if __name__ == "__main__":
    unittest.main()