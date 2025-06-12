# CinePy
### **Test Your Movie Knowledge Like Never Before!**
#### **Video Demo:** [Watch on YouTube](https://youtu.be/FVnPspVhYgQ)

### **Overview**
*Cinephile* is a game designed for movie lovers who want to dive deep into cinema trivia. Whether you’re a casual fan or a full-blown film buff, this game will challenge your knowledge of films, actors, directors, and plots. Think you know the classics? Let's put that to the test!

### **Languages & Tools Used**
The game is powered by **Python** and the versatile **IMDbPy** library, which offers detailed movie information such as plots, cast lists, and crew members. Crafting Cinephile was no easy feat: I immersed myself in Python syntax, algorithms, and IMDbPy’s documentation to bring this idea to life.

Using IMDbPy, I curated a selection of movies from IMDb’s Top 250 Films of All Time. Then, I crafted a dictionary with each movie’s title as the key and its IMDb ID as the value, allowing the game to randomly select a new movie for each round. Combined with Python’s **random** library, this setup ensures no two games are the same—every playthrough feels fresh and exciting.

### **Gameplay**
In *Cinephile*, your goal is to guess the movie title based on a series of clues. Each game consists of **three rounds**, each with **three parts** that progressively reveal hints about a randomly selected movie.

**Round Structure:**

1. **Part 1: Plot Guessing**
   - A few sentences describing the plot appear on the screen. Guess the movie correctly at this stage, and you’ll score **20 points**.
   - Incorrect guesses? No worries—you’ll get two more chances in Part 1.
   - If you still can’t guess it, you’ll lose 10 points and move on to Part 2.

2. **Part 2: Famous Cast Members**
   - Here, you’ll see a list of the movie’s main actors and actresses.
   - Guess correctly to earn **10 points**.
   - Two chances are allowed in this part, but failing here deducts 5 points and sends you to Part 3.

3. **Part 3: Director Clue**
   - Now you get one final clue—the name of the movie's director.
   - Guess correctly for **5 points**.
   - No points are awarded if you miss the guess in this part.

After three rounds, your total score is displayed, along with a cinematic dragon animation to wrap things up in style!

### **Future Plans**
The game has tons of potential, and I already have exciting ideas for enhancing it:

1. **Graphical User Interface (GUI)**
   - Instead of playing in the terminal, a user-friendly interface would add style and make the game more interactive and accessible for everyone.

2. **Player Database & Leaderboard**
   - Integrating a database would allow us to track players’ scores, making *Cinephile* a competition. Imagine a global leaderboard where cinephiles from around the world compete for the top spot!

### **Join the Fun**
Do you think you have what it takes to be considered a cinephile? Step into the world of movies and challenge yourself with clues from some of the greatest films in cinema.
