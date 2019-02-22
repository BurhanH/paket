import paket
import unittest


class Test(unittest.TestCase):
    def test_paket(self):
        self.assertEqual(paket.get(), u'Here is our message for an example!')


if __name__ == '__main__':
    unittest.main()
