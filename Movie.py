import fresh_tomatoes

class Movie():

        def __init__ (self, title, poster_image_url, trailer_youtube_url):
                self.title = title
                self.poster_image_url = poster_image_url
                self.trailer_youtube_url = trailer_youtube_url

terminal = Movie("Terminal","http://movizland.com/wp-content/uploads/terminal_ver2.jpg","https://www.youtube.com/watch?v=ciByvddyHBs")
toy_story = Movie("Toy Story","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg","https://www.youtube.com/watch?v=4KPTXpQehio")
nemo = Movie("The Finding Nemo","https://www.kids.almo7eb.com/thumbs/nemo-8344537722.jpg","https://www.youtube.com/watch?v=wZdpNglLbt8")
iron_giant = Movie("The Iron Giant","http://t1.gstatic.com/images?q=tbn:ANd9GcRCwz75tuERvCFpNaHIeuqr6NSh_KjdfCxcq3i2M3u47FQBI0AS","https://www.youtube.com/watch?v=JgjmFBX34zc")
bambi = Movie("Bambi ","https://www.kids.almo7eb.com/thumbs/bambi-1-1124813351.jpg","https://www.youtube.com/watch?v=suAZVUatuH0")
incredibles = Movie("The Incredibles","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXYncfHfNmFpDBk7CYQ9KDQCu9FdZjyXsvPr2Ip8VqVghScLZm7Q","https://www.youtube.com/watch?v=ZJDMWVZta3M")

movies = [terminal, toy_story, nemo, iron_giant, bambi, incredibles]

fresh_tomatoes.open_movies_page(movies)
