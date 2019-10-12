import media
import home_movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

equalizer2 = media.Movie("The Equalizer2", "A retired officer bringing justice to light",
                         "http://cdn.collider.com/wp-content/uploads/2018/04/equalizer-2-denzel-washington.jpg",
                         "https://www.youtube.com/watch?v=eAKrgwCnkGM")

movies = [toy_story, avatar, equalizer2]
home_movies.open_movies_page(movies)
# print(dir(media.Movie))
