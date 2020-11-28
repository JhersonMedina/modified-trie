from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['input']
	processed_text = text.upper()
	print(processed_text)
	return processed_text

