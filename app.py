from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import re

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/xplrdotio')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
emails = db['emails']
locations = db['locations']


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

@app.route('/signed-up/<is_email_valid>')
def signed_up_function(is_email_valid):
	"""Show thank-you page."""

	print("Is email valid? : {}".format(is_email_valid))

	return render_template("signed_up.html", is_email_valid=is_email_valid)

@app.route('/signed-up', methods=['POST'])
def add_email_function():
	"""Add new email to emails model."""

	input_email = {
		'email': request.form.get("email")
	}

	print("This is the email that I got: {}".format(input_email['email']))

	is_email_valid = validate_email(input_email)

	print("Email validity: {}".format(is_email_valid))

	if is_email_valid:
		emails.insert_one(input_email)

	return redirect(url_for("signed_up_function", is_email_valid=is_email_valid))

def validate_email(input_email):
	is_email_valid = False
	if '@' in str(input_email) and len(list(input_email)) > 0:
		is_email_valid = True
	return is_email_valid


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
