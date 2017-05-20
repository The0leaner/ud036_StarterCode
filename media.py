import webbrowser
class Movie():
    """here is my movie class
	args:
	valid_ratings(list): include Movie Rating System's different levels
	"""
    valid_ratings = {"G", "PG", "PG-13", "R"}
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
	"""init method
	args:
	movie_title(str): a movie's title
	movie_storyline(str): summary about the movie
	poster_image(str): an url link to special movie poster pic
	trailer_youtube(str): an url link to movie's youtube play 
	"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
	"""
	import webbrowser to open movie's youtube url link
	"""
        webbrowser.open(self.trailer_youtube_url)
