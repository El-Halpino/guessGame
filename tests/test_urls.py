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