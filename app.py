from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient()
xplrdotio = client['xplrdotio']
emails = xplrdotio['emails']
locations = xplrdotio['locations']


@app.route('/')
def home_function():
	"""Show home page."""

	return render_template("home.html")

@app.route('/about')
def about_function():
	"""Show about/features page."""

	return render_template("about.html")

@app.route('/interested')
def interested_function():
	"""Show interested page."""

	return render_template("interested.html")

@app.route('/signed-up')
def signed_up_function():
	"""Show thank-you page ."""

	pass

@app.route('/signed-up', methods=['POST'])
def add_email_function():
	"""Add new email to emails model."""

	pass


if __name__ == "__main__":
	app.run(debug=True)
