import unittest
from random_password.password import Password


class TestPassword(unittest.TestCase):

    def test_generate_32(self):
        pwd = Password()
        passphrase = pwd.generate(32)
        print(passphrase)
        self.assertEqual(len(passphrase), 32)


if __name__ == '__main__':
    unittest.main()
