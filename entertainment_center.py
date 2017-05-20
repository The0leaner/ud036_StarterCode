import media
import fresh_tomatoes

""" Puttinng some movies' details
    movies ：a list of instances of Movie
 """
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/"
    "Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)
avater = media.Movie(
    "Avater",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/id/b/b0/"
    "Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=-9ceBgWV8io")
school_of_rock = media.Movie(
    "School of Rock",
    "A story of a boy play rock in campus",
    "https://upload.wikimedia.org/wikipedia/en/1/11/"
    "School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie(
    "Ratatouille",
    "A storyline is waiting",
    "https://upload.wikimedia.org/wikipedia/en/5/50/"
    "RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Paris Story",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/"
    "Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=-9ceBgWV8io")
wild_child = media.Movie(
    "Wild Child",
    "storyline",
    "https://upload.wikimedia.org/wikipedia/commons/7/76"
    "/Wild_Child.jpg",
    "https://www.youtube.com/watch?v=v2oC2vJailQ")
# print(wild_child.storyline)
# self.show_trailer()
# print(media.Movie.valid_ratings)
movies = [toy_story, avater, school_of_rock, ratatouille, \]
[midnight_in_paris, wild_child]
fresh_tomatoes.open_movies_page(movies)
