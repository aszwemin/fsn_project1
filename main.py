"""Main file to run the movies website.
It creates a list of movies and calls the function to display them
"""

import sys
from media import Movie
from fresh_tomatoes import open_movies_page


# ValidationError to be raised when incorrect text file supplied
class ValidationError(Exception):
    pass


def init(movies_path):
    """Function to initialize the data for the application.

    Parameters:
    - movies_path - path to a file from which the initial data should
    be taken

    Returns: a list of Movie objects
    """
    try:
        # Open file specified in movies_path and populate movies list
        with open(movies_path) as movies_file:
            movies_list = []
            # Get contents of the file by lines
            contents = movies_file.readlines()
            for movie in contents:
                # Strip newline and split by comma
                movie_details = movie.rstrip().split(',')
                if len(movie_details) != 5:
                    raise ValidationError('Incorrect number of movie details')
                # Instantiate Movie class and append it to the list
                movies_list.append(Movie(*movie_details))

        if not movies_list:
            raise ValidationError('Empty file')

        return movies_list
    except IOError:
        raise ValidationError('No such file')


# When this file is called from the command line, initialize and 
# call open_movies_page with the list of movies
if __name__ == '__main__':
    # if the file path argument supplied, use it, else default
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = 'movies.txt'
    # initialize with the contents of the file
    try:
        movies = init(file_path)
    except ValidationError as e:
        print 'Provided text file is incorrect: ' + str(e)
    else:
        open_movies_page(movies)
