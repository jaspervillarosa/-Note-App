import unittest
from villarosa_notes import Note_Keeping_App


class TestKeepNote(unittest.TestCase):
    def test_notes(self):
        #arrange
        #act
        #assert
        self.assertEqual([obj.date, obj.description],
                         ["March 28 2000", "Practicum" , "Doing assignment", "Active"])


obj = Note_Keeping_App("March 28 2000", "Practicum" , "Doing assignment", "Active")

if __name__ == '__main__':
    unittest.main()