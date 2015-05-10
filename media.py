"""File defining datastructures for the application
"""


class Movie(object):
    """Movie class storing information about a given movie

    Parameters:
    - title - title of the movie
    - poster_url - url to the poster to be displayed for the movie
    - youtube_url - url to youtube trailer of the movie
    - release_date - release date of the movie
    - rating - rating of the movie
    """

    # British rating categories
    RATINGS = ['U', 'PG', '12A', '15', '18', 'R18']

    def __init__(self, title, poster_url, youtube_url, release_date, rating):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
        self.release_date = release_date
        if rating in Movie.RATINGS:
            self.rating = rating
        else:
            self.rating = 'N/A'
