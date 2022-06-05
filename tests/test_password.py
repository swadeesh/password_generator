import unittest
import random_password
from random_password.password import Password


class TestPassword(unittest.TestCase):

    def test_generate_32(self):
        pwd = Password()
        passphrase = pwd.generate(32)
        self.assertEqual(passphrase.length(), 30)


if __name__ == '__main__':
    unittest.main()
