# Importing needed libraries like imdb library for using its database of movies
import imdb
import random
import cowsay

# Declaring needed variables
TOP250 = []
ID = {}
TOTAL_SCORE = 0
ROUND_NUMBER = 1
ROUND_SCORE = 0
COUNT = 0


# Using different syntax of imdb library in order to create a list of the names of the Top 250 Movies of All Time and a dictionary with the names and their IDs
OBJECT = imdb.IMDb()
MOVIE = OBJECT.get_top250_movies()
for ITEM in MOVIE:
    TOP250.append(ITEM["title"])
    ID.update({ITEM["title"]: ITEM.movieID})


# Starting the programming with some user friendly questions and conversation
print("Hi...")
NAME = input("What's your name?\n")
print("Welcome to the game, %s. I assume you've seen so many movies, haven't you? (Yes/No)" %NAME)
YESNO = input()
if "no" in YESNO.lower():
    print("Sad to hear that. I guess we need to say goodbye because I don't think you can survive this challenge. Farewell, dear %s." %NAME)
    exit()
print("Now I'm going to give you the game instructions. After that, we start our journey.")


# Giving the instructions of the game
print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print("Description:")
print("I'm going to give to the synopsis of a movie selected from the Top 250 Movies of All Time. Then you have to guess what movie it is. If your answer is wrong, you have two more chances to guess. After that, if wrong again, I help you with more guidence, however, you lose score. After helping you for the second time, then you have 2 chances to guess. if you can't answer correctly, then you will lose score again and I help you again by giving more information. This time, you only have one time to guess. If you can't guess the movie, you don't get any point and then you go into the next round. The game will be played in 3 rounds. After the final round, we'll show you your final score which is the combination of your score in each round. That's it. That's the game. It's time to prove you're a big fan of movies. Keep in mind that even if you guess only a word of the movie name, you win the round. Let the game begin")
print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print("If you're ready to start the game, please type Yes and wait for a couple of seconds. (Yes)")
YES = ""
while YES.title() != "Yes":
    YES = input()


# A loop to make sure there will be three rounds for the game
while COUNT != 3:
    print("------------------------------------------")
    print("------------------------------------------")
    print("ROUND NUMBER %i" %ROUND_NUMBER)
    F1 = True
    F2 = True
    F3 = True
    CAST = []
    COUNT1 = 0
    COUNT2 = 0
    COUNT3 = 0


    # Creating different variables to have the plot, the director and the cast of our random-picked movie
    R = random.randrange(0, len(TOP250))
    MOVIE_ID = ID[TOP250[R]]
    MOVIE_NAME = TOP250[R]
    MOVIE_INFO = OBJECT.get_movie(MOVIE_ID)
    MOVIE_PLOT = MOVIE_INFO["plot"][0]
    CUTTER = MOVIE_PLOT.find(":")
    SYNOPSIS = MOVIE_PLOT[:CUTTER]
    DIRECTOR = MOVIE_INFO["director"][0]["name"]
    for i in range(5):
        CAST.append(MOVIE_INFO["cast"][i]["name"])


    # Part I of the game which is giving the plot
    print("------------------------------------------")
    print("PART I")
    print("Here is the plot of the movie:")
    print(SYNOPSIS)
    print("------------------------------------------")
    print("Can you guess what movie it is?")
    COUNT4 = 2
    while F1 == True:
        NAME_MOVIE1 = input()
        if NAME_MOVIE1.title() in MOVIE_NAME.title():
            print("AMAZING, %s! YOU WON! YOU GET 20 POINTS FOR THIS ROUND!" %NAME)
            COUNT += 1
            ROUND_NUMBER += 1
            ROUND_SCORE = 20
            F2 = False
            F3 = False
            break
        else:
            if COUNT4 != 0:
                print("You have %i more chance(s) to guess. Try again, pal." %COUNT4)
        COUNT4 -= 1
        COUNT1 += 1
        if COUNT1 == 3:
            F1 = False


    # Part II of the game which is giving the names of the actors/actresses
    if F2 == True:
        print("------------------------------------------")
        print("PART II")
        print("You couldn't guess correctly with the help of the plot of the movie. You lost 10 points and now I give you the name of the 5 of the most famous actors/actresses of this movie.")
        print("The Cast: %s | %s | %s | %s | %s" %(CAST[0], CAST[1], CAST[2], CAST[3], CAST[4]))
        print("------------------------------------------")
        print("What about now? Can you guess what movie it is this time?")
        COUNT4 = 1
    while F2 == True:
         NAME_MOVIE2 = input()
         if NAME_MOVIE2.title() in MOVIE_NAME.title():
            print("CONGRATS, %s! RIGHT! YOU GET 10 POINTS FOR THIS ROUND!" %NAME)
            COUNT += 1
            ROUND_NUMBER += 1
            ROUND_SCORE = 10
            COUNT3 = 3
            F3 = False
            break
         else:
             if COUNT4 != 0:
                print("You have %i more chance(s) to guess. Try again, pal." %COUNT4)
         COUNT4 -= 1
         COUNT2 += 1
         if COUNT2 == 2:
             F2 = False


    # Part III of the game which is giving the name of the director
    if F3 == True:
        print("------------------------------------------")
        print("PART III")
        print("This is the last time I help you. Be careful. You lost 5 more points and now you have 5 points in hand if you guess the movie in this level. Now I give you the name of the director.")
        print("The Director: " + DIRECTOR)
        print("------------------------------------------")
        print("This is your last chance. Think, think, think. What is the name of the movie?")
        COUNT4 = 0
    while F3 == True:
         NAME_MOVIE3 = input()
         if NAME_MOVIE3.title() in MOVIE_NAME.title():
            print("FINALLY, %s! YES! YOU GET 5 POINTS FOR THIS ROUND!" %NAME)
            COUNT += 1
            ROUND_NUMBER += 1
            ROUND_SCORE = 5
            F4 = True
            break
         else:
             if COUNT4 != 0:
                print("You have %i more chance(s) to guess. Try again, pal." %COUNT4)
         COUNT4 -= 1
         COUNT3 += 1
         if COUNT3 == 1:
             F3 = False
             COUNT += 1
             ROUND_NUMBER += 1
             ROUND_SCORE = 0
             print("OH! YOU LOST! YOU GET NO POINT ON THIS ROUND!")
    TOTAL_SCORE += ROUND_SCORE


# The final part after finishing all three rounds and printing the calculated total point of the player
print("------------------------------------------")
print("------------------------------------------")
cowsay.dragon("THANK YOU FOR PLAYING, DEAR %s.\nYOUR TOTAL POINT IS %i.\nGOODBYE.\n\n\n<POWERED BY AMIR MASOUD ALMASI>" %(NAME.upper(), TOTAL_SCORE))
print("------------------------------------------")
print("------------------------------------------")