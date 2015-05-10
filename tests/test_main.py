"""Test contents of main.py"""
import unittest
from ..main import init, ValidationError


class TestInit(unittest.TestCase):
    def test_init(self):
        init('movies/tests/movies.txt')

    def test_init_empty_file(self):
        with self.assertRaises(ValidationError) as e:
            init('movies/tests/movies_empty.txt')

        self.assertIn('Empty file', e.exception)

    def test_init_invalid_file(self):
        with self.assertRaises(ValidationError) as e:
            init('movies/tests/movies_invalid.txt')

        self.assertIn('Incorrect number of movie details', e.exception)

    def test_init_no_such_file(self):
        with self.assertRaises(ValidationError) as e:
            init('movies/tests/moviesx.txt')

        self.assertIn('No such file', e.exception)


if __name__ == '__main__':
    unittest.main()
