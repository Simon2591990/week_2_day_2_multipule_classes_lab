import unittest
from src.person import Person
# from tests.person_test import TestPerson

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, "Ocean Terminal" )
        #self.guido = Person("Guido van Rossum", 64, "Ocean Terminal" )

    #@unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    #@unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)
