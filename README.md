Movie Trailer Application
=========================

Description
-----------

This application takes movies' definition from a text file
and generates a page showing all the movies with their posters,
titles, release dates and rating. When a user clicks on the 
movie poster, a modal with the movie's trailer will be shown.
Ratings are shown in the British ratings classification and 
if the one in the text file doesn't match it, it will be shown
as N/A.

If the file describing the movies is invalid, a Validation will be 
raised. The format of the files is as follows:

> title,poster_url,trailer_url,release_date,rating

Each line in the text file represents one movie

How to run
----------

From the command line run the following:

> python main.py

This will open the page with movies specified in movies.txt file.
A different file can be used by specifying it as a first argument:

> python main.py other_file.txt

Testing
-------

There are tests provided for the media.py and main.py files, which
can be found in the test directory. To run tests do one of the following:

1. Install nose (`pip install nose`) and run `nosetests` in the folder containing the movies folder
2. Run each test file separately from a folder containing movies (e.g. `python -m movies.tests.test_media`)
