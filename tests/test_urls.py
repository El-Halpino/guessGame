from flask import request, session

def test_app(app):
    assert app.secret_key == "wrrrrrfegko3245tk50ekdgrge3t2ewdsf"

def test_up(client):
    assert client.get("/").status_code != 404

def test_guessform(client):
    response = client.get("/guessform")
    assert response.status_code == 200
    assert response.data.startswith(b"<!DOCTYPE html>") == True
    assert b'<form method="POST" action="/90logic">' in response.data

def test_highscore(client):
    response = client.get("/highScore")
    assert response.status_code == 200
    assert response.data.startswith(b"<!DOCTYPE html>") == True

def test_high(client):
    with client.session_transaction() as sess:
        sess["number"] = 1
        sess["numOfGuesses"] = 1
    response = client.post("/90logic", data={"userGuess": 2})
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data
    assert b"Too High!" in resp

def test_low(client):
    with client.session_transaction() as sess:
        sess["number"] = 2
        sess["numOfGuesses"] = 1
    response = client.post("/90logic", data={"userGuess": 1})
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data
    assert b"Too Low!" in resp

def test_correct(client):
    with client.session_transaction() as sess:
        sess["number"] = 1
        sess["numOfGuesses"] = 1
    response = client.post("/90logic", data={"userGuess": 1})
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data
    assert b"You Guessed it!" in resp

def test_leaderboard_insert(client):
    with client.session_transaction() as sess:
        sess["number"] = 1
        sess["numOfGuesses"] = 1
        sess["start"] = 1
        sess["end"] = 10
    response = client.post("/setHighScore", data={"userName": "test_user"})
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data
    assert b"You are rank" in resp