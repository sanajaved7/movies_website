import fresh_tomatoes
import media

# Creating multiple instances of class Movie to display on website
toy_story = media.Movie(
    "Toy Story",
    '''A cowboy doll is profoundly threatened and jealous when a
    new spaceman figure supplants him as top toy in a boy's room.''',
    "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

groove = media.Movie(
    "Emperor's New Groove",
    '''Emperor Kuzco is turned into a llama by his ex-administrator
    Yzma, and must now regain his throne with the help of Pacha,
    the gentle llama herder.''',
    "http://bit.ly/1EnEWFp",
    "https://www.youtube.com/watch?v=t_YjSbp5KHM")

shawshank = media.Movie(
    "The Shawshank Redemption",
    '''Two imprisoned men bond over a number of years, finding solace
    and eventual redemption through acts of common decency.''',
    "http://www.movie-list.com/img/posters/big/zoom/shawshankredemption.jpg",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

avengers = media.Movie(
    "Avengers: Age of Ultron",
    '''When Tony Stark and Bruce Banner try to jump-start a
    dormant peacekeeping program called Ultron, things go horribly
    wrong and it's up to Earth's Mightiest Heroes to stop the villainous
    Ultron from enacting his terrible plans.''',
    "http://bit.ly/1EnEWFp",
    "https://www.youtube.com/watch?v=JAUoeqvedMo")

finding_nemo = media.Movie(
    "Finding Nemo",
    '''After his son is captured in the Great Barrier Reef and taken
    to Sydney, a timid clownfish sets out on a journey to bring him home.''',
    "http://bit.ly/1J0Z1qj",
    "https://www.youtube.com/watch?v=wZdpNglLbt8")

titanic = media.Movie(
    "Titanic",
    '''A seventeen-year-old aristocrat, expecting to be married to a rich
     claimant by her mother, falls in love with a kind but poor artist
     aboard the luxurious, ill-fated R.M.S. Titanic.''',
    "http://bit.ly/1bkMsci",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

# Passing in movies array to fresh_tomatoes open_movies_page function
movies = [toy_story, groove, shawshank, avengers, finding_nemo, titanic]
fresh_tomatoes.open_movies_page(movies)
