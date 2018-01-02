import fresh_tomatoes


class Movie():
	""" The class will be used to create instances of Movie object """

        def __init__(self, title, poster_image_url, trailer_youtube_url):
                """ Predefined function to set the instance variables of Movie Class """
            self.title = title
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url

# Terminal movie: movie title, movie poster image url, movie youtube trailer url
terminal = Movie(
"Terminal", 
"http://movizland.com/wp-content/uploads/terminal_ver2.jpg", 
"https://www.youtube.com/watch?v=ciByvddyHBs")

# Toy story movie: movie title, movie poster image url, movie youtube trailer url
toy_story = Movie(
"Toy Story", 
"https://goo.gl/bj4aZS", 
"https://www.youtube.com/watch?v=4KPTXpQehio")

# The Finding Nemo movie: movie title, movie poster image url, movie youtube trailer url
nemo = Movie(
"The Finding Nemo", 
"https://www.kids.almo7eb.com/thumbs/nemo-8344537722.jpg", 
"https://www.youtube.com/watch?v=wZdpNglLbt8")

# The Iron Giant movie: movie title, movie poster image url, movie youtube trailer url
iron_giant = Movie(
"The Iron Giant", 
"https://goo.gl/CP5Pfz", 
"https://www.youtube.com/watch?v=JgjmFBX34zc")

# Bambi movie: movie title, movie poster image url, movie youtube trailer url
bambi = Movie(
"Bambi", 
"https://goo.gl/YBdhzS", 
"https://www.youtube.com/watch?v=suAZVUatuH0")

# The Incredibles movie: movie title, movie poster image url, movie youtube trailer url
incredibles = Movie(
"The Incredibles", 
"https://goo.gl/rU9u8d", 
"https://www.youtube.com/watch?v=ZJDMWVZta3M")

# Array of movies that will be passed to open movies function
movies = [
	terminal, 
	toy_story, 
	nemo, 
	iron_giant, 
	bambi, 
	incredibles
	]

# Open movies page in the a web browser to display movies list
fresh_tomatoes.open_movies_page(movies)
