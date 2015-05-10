import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

groove = media.Movie("Emperor's New Groove","Emperor Kuzco is turned into a llama by his ex-administrator Yzma, and must now regain his throne with the help of Pacha, the gentle llama herder.", "https://fanart.tv/fanart/movies/11688/movieposter/the-emperors-new-groove-52ee9b3293a65.jpg","https://www.youtube.com/watch?v=t_YjSbp5KHM")

shawshank = media.Movie("The Shawshank Redemption","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "http://www.movie-list.com/img/posters/big/zoom/shawshankredemption.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

avengers = media.Movie("Avengers: Age of Ultron","When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it's up to Earth's Mightiest Heroes to stop the villainous Ultron from enacting his terrible plans.", "http://ia.media-imdb.com/images/M/MV5BMTU4MDU3NDQ5Ml5BMl5BanBnXkFtZTgwOTU5MDUxNTE@._V1_SY317_CR1,0,214,317_AL_.jpg","https://www.youtube.com/watch?v=JAUoeqvedMo")

finding_nemo = media.Movie("Finding Nemo","After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.", "http://ia.media-imdb.com/images/M/MV5BMTY1MTg1NDAxOV5BMl5BanBnXkFtZTcwMjg1MDI5Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg","https://www.youtube.com/watch?v=wZdpNglLbt8")

titanic = media.Movie("Titanic","A seventeen-year-old aristocrat, expecting to be married to a rich claimant by her mother, falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.", "http://ia.media-imdb.com/images/M/MV5BMjExNzM0NDM0N15BMl5BanBnXkFtZTcwMzkxOTUwNw@@._V1_SY317_CR0,0,214,317_AL_.jpg","https://www.youtube.com/watch?v=zCy5WQ9S4c0")

movies = [toy_story, groove, shawshank, avengers, finding_nemo, titanic]
fresh_tomatoes.open_movies_page(movies)
