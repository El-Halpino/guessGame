from flask import Flask, render_template, request, session
import random
import time
import pickle

app = Flask(__name__)

@app.route("/guessform")
def start_guessForm():
    session["number"] = random.randint(1, 1000)
    session["numOfGuesses"] = 0
    session["start"] = time.perf_counter()
    return render_template("guessform.html", the_title="Guessing Game")


@app.route("/90logic")
def do_logic():
    guess = int(request.form["userGuess"])
    ##return render_template("guessform.html", value = guess) send value guess back to html
    if guess == session["number"]:
        session["end"] = time.perf_counter()
        return render_template("correctGuess.html", the_title="You Guessed it!")
    elif guess > session["number"]:
        session["numOfGuesses"] + 1
        return render_template("tooHigh.html", the_title="Too High!")
    elif guess < session["number"]:
        session["numOfGuesses"] + 1
        return render_template("tooLow.html", the_title="Too Low!")

@app.route("/setHighScore", methods=["POST", "GET"])
def record_highscore():
    name = str(request.form["userName"])
    time = round(session["end"] - session["start"], 2)
    userRecord = [name, session["numOfGuesses"], time]
    with open("records.pickle", "rb") as pf:
        try:
            highScores = list(pickle.load(pf))
        except:
            highScores = list()
highScores = list()        
highScores.append(userRecord) 
finalHighScores = sorted(highScores)

rank = (
    sorted(highScores).index([name, session["numOfGuesses"], time]) + 1
)




##app.route("/highScore")
##def display_highScore():
##    score = session["score"]
##
##    return render_template(
##        "highScore.html", the_title="HighScores!", the_data=sorted(data, reverse=True)
##   )
##
##app.route("/storeResults")
##def store_results():

app.secret_key = "wrrrrrfegko3245tk50ekdgrge3t2ewdsf"

if __name__ == "__main__":
    app.run(debug=True)