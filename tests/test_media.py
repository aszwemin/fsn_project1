"""Test contents of media.py"""
import unittest
from ..media import Movie


class TestMovie(unittest.TestCase):
    def test_creation(self):
        movie = Movie(
            'title', 'pic_url', 'youtube_url', 'date', '12A'
        )
        self.assertEqual(movie.title, 'title')
        self.assertEqual(movie.poster_image_url, 'pic_url')
        self.assertEqual(movie.trailer_youtube_url, 'youtube_url')
        self.assertEqual(movie.release_date, 'date')
        self.assertEqual(movie.rating, '12A')

    def test_rating_invalid(self):
        movie = Movie(
            'title', 'pic_url', 'youtube_url', 'date', 'rating'
        )
        self.assertEqual(movie.rating, 'N/A')


if __name__ == '__main__':
    unittest.main()
