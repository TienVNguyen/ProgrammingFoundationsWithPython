import Lession6_Movie
import fresh_tomatoes

toy_story = Lession6_Movie.Movie("Toy Story",
                                 "A story of a boy and his toys that come to life",
                                 "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                 "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = Lession6_Movie.Movie("Avatar",
                              "A marine on an alient planet",
                              "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                              "https://www.youtube.com/watch?v=-9ceBgWV8io")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
