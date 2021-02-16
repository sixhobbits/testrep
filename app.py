from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
	return redirect(url_for('main'))

@app.route('/main')
def main():
	return render_template("index.html")
