import media
import fresh_tomatoes

# Create instances of Movie class
let_the_bullets_fly = media.Movie("Let the Bullets Fly",
                                  "A comedy happened in China in 1920s",
                                  "http://www.cinefish.bg/data/movies_images/103/p_103941.jpg",
                                  "https://www.youtube.com/watch?v=PFoLfRA5ghw")
v_for_vendetta = media.Movie("V for Vendetta", 
                             "A story of a shadowy freedom fighter",
                             "http://img3.douban.com/view/photo/raw/public/p2180077575.jpg",
                             "https://www.youtube.com/watch?v=k_13fFIrhPk")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back to 1920s to meet writers",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
before_sunrise = media.Movie("Before Sunrise",
                             "A 'walking and talking' romantic story",
                             "http://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                             "https://www.youtube.com/watch?v=9v6X-Dytlko")
lock_stock_barrels = media.Movie("Lock, Stock and Two Smoking Barrels",
                                 "A series of unexpected events",
                                 "http://www.impawards.com/1999/posters/lock_stock_and_two_smoking_barrels_ver1_xlg.jpg",
                                 "https://www.youtube.com/watch?v=qi_VQRyxJ2Y")
litte_nicholas = media.Movie("Little Nicholas",
                             "A young boy's story full of fun",
                             "http://iv1.lisimg.com/image/724746/600full-little-nicholas-poster.jpg",
                             "https://www.youtube.com/watch?v=mZHNjPvLpNw")

# Create a list of Movie's instances
movies = [let_the_bullets_fly, before_sunrise,litte_nicholas, v_for_vendetta, lock_stock_barrels, midnight_in_paris]

# Open the page in the browser
fresh_tomatoes.open_movies_page(movies)