import fresh_tomatoes
import media

#
# This program created a number of movie objects. Each object contains:
# Title, Plot Summary, link to a movie poster and a Youtube trailer
# 
#
# Three files are requred for this program to function:
# entertainment_center.py media.py fresh_tomatoes.py
# 
#   Konrad Trybulski         2/25/2015
#


# Create a object instance for each movie
tommy_boy = media.Movie("Tommy Boy",
                        "After his beloved father dies, dimwitted Tommy Callahan inherits a near-bankrupt automobile parts factory in Sandusky, Ohio.",
                        "pics\Tommy_Boy_Poster.jpg",
                        "www.youtube.com/watch?v=6nQ4K2bvVxY")

hunger_games = media.Movie("Hunger Games",
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.",
                           "pics\Hunger_Games_Poster.jpg",
                           "http://www.youtube.com/watch?v=PbA63a7H0bo")

princess_bride = media.Movie("Princess Bride",
                           "A fairy tale adventure about a beautiful young woman and her one true love.",
                           "pics\Princess_Bride_Poster.jpg",
                           "https://www.youtube.com/watch?v=VYgcrny2hRs")

american_sniper = media.Movie("American Sniper",
                     "U.S. Navy SEAL Chris Kyle takes his sole mission - protect his comrades",
                     "pics\American_Sniper_Poster.jpg",
                     "https://www.youtube.com/watch?v=99k3u9ay1gs")

christmas_vacation = media.Movie("Christmas Vacation",
                                 "As the holidays approach, Clark Griswold (Chevy Chase) wants to have a perfect family Christmas",
                                 "pics\Christmas_Vacation_Poster.jpg",
                                 "https://www.youtube.com/watch?v=NBTTipJX-h4")

spaceballs = media.Movie("Spaceballs",
                         "Planet Spaceball's President Skroob sends Lord Dark Helmet to steal Planet Druidia's abundant supply of air to replenish their own, and only Lone Starr can stop them.",
                          "pics\Spaceballs_Poster.jpg",
                          "www.youtube.com/watch?v=0uzEgsHypgM")

beer_wars = media.Movie("Beer Wars",
                        "Storyline",
                        "pics\Beer_Wars_Poster.jpg",
                        "www.youtube.com/watch?v=uY-Bg5Odi0M")

hangover = media.Movie("The Hangover",
                  "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.",
                  "pics\Hangover_Poster.jpg",
                  "www.youtube.com/watch?v=vhFVZsk3XEs")

se7en = media.Movie("Se7en",
                  "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi.",
                  "pics\Se7en_Poster.jpg",
                  "www.youtube.com/watch?v=J4YV2_TcCoE")




# Create a list with objects - movies
movies = [tommy_boy, hunger_games, princess_bride, american_sniper, christmas_vacation, spaceballs, beer_wars, hangover, se7en]

# Pass the list of movies to module which will create a web site and launch a browser 
fresh_tomatoes.open_movies_page(movies)

