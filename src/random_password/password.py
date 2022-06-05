import string
import random
from multipledispatch import dispatch


class Password:
    def __init__(self):
        # characters to generate password from
        self.alphabets = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.special_characters = list("!@#$%^&*()")
        self.characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    @dispatch(int)
    def generate(self, length):
        # length of password from the user
        if length <= 0:
            raise Exception("Password length must be a positive number.")

        # shuffling the characters
        random.shuffle(self.characters)

        # picking random characters from the list
        password = []

        # picking random alphabets
        for i in range(length):
            password.append(random.choice(self.characters))

        # shuffling the resultant password
        random.shuffle(password)

        # converting the list to string
        # printing the list
        return "".join(password)

    @dispatch(int, int, int)
    def generate(self, alphabets_count, digits_count, special_characters_count):
        # number of character types
        if alphabets_count <= 0:
            raise Exception('Alphabets count must be a positive number.')

        # number of digits
        if digits_count <= 0:
            raise Exception('Digits count must be a positive number.')

        # number of special characters
        if special_characters_count <= 0:
            raise Exception('Special characters count must be a positive number.')

        characters_count = alphabets_count + digits_count + special_characters_count

        # initializing the password
        password = []

        # picking random alphabets
        for i in range(alphabets_count):
            password.append(random.choice(self.alphabets))

        # picking random digits
        for i in range(digits_count):
            password.append(random.choice(self.digits))

        # picking random alphabets
        for i in range(special_characters_count):
            password.append(random.choice(self.special_characters))

        # shuffling the resultant password
        random.shuffle(password)

        # converting the list to string and return
        return "".join(password)
