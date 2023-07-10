import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # The value is 'Leo'
    message = request.form['message']

    # Send back a fond farewell with the name
    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name'] # The value is 'Leo'

    # Send back a friendly greeting with the name
    return f"I am waving at {name}"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text =request.form['text']
    n = 0
    for letter in text:
        if letter in 'aeiouAEIOU':
            n+=1
    return f'There are {n} vowels in "{text}"'

@app.route('/names', methods=['GET'])
def names():
    name1 = request.args['name']
    newlist = name1.split(',')
    namelist =['Julia', 'Alice', 'Karim']
    for name in newlist:
        namelist.append(name)
    namelist.sort()
    string= ', '.join(namelist)
    return string


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
