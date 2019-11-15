from flask import Flask, render_template, request, session
import random
import time
import pickle

app = Flask(__name__)


@app.route("/")
def def_screen():
    return "Enter /guessform to start game.\nEnter /highScore to view the leaberboards"


@app.route("/guessform")
def start_guessForm():
    session["number"] = random.randint(1, 1000)
    session["numOfGuesses"] = 0
    session["start"] = time.perf_counter()
    return render_template("guessform.html", the_title="Guessing Game")


@app.route("/90logic", methods=["POST"])
def do_logic():
    guess = int(request.form["userGuess"])
    if guess == session["number"]:
        session["end"] = time.perf_counter()
        return render_template("correctGuess.html", the_title="You Guessed it!")
    elif guess > session["number"]:
        numOfGuesses1 = int(session["numOfGuesses"])
        numOfGuesses1 = numOfGuesses1 + 1
        session["numOfGuesses"] = str(numOfGuesses1)
        return render_template(
            "guessform.html", the_title="Too High!", currentStatus="Too High!"
        )
    elif guess < session["number"]:
        numOfGuesses1 = int(session["numOfGuesses"])
        numOfGuesses1 = numOfGuesses1 + 1
        session["numOfGuesses"] = str(numOfGuesses1)
        return render_template(
            "guessform.html", the_title="Too Low!", currentStatus="Too Low!"
        )


@app.route("/highScore")
def display_highScore():
    with open("records.pickle", "rb") as pf:
        data = sorted(pickle.load(pf), reverse=True)
    return render_template("highScore.html", the_title="HighScores!", myHighScores=data)


@app.route("/setHighScore", methods=["POST", "GET"])
def record_highscore():
    name = request.form["userName"]
    time = round(session["end"] - session["start"], 2)
    time = str(time)
    userRecord = [time, session["numOfGuesses"], name]
    with open("records.pickle", "rb") as pf:
        try:
            highScores = list(pickle.load(pf))
        except:
            highScores = list()
    highScores.append(userRecord)
    finalHighScores = sorted(highScores)
    rank = finalHighScores.index([time, session["numOfGuesses"], name]) + 1
    with open("records.pickle", "wb") as pf:
        pickle.dump(highScores, pf)
        return render_template(
            "gameComplete.html", the_title="Guessing Game", position=rank
        )


app.secret_key = "wrrrrrfegko3245tk50ekdgrge3t2ewdsf"

if __name__ == "__main__":
    app.run(debug=True)
