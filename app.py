from flask import Flask, request, redirect

app = Flask(_name_)

@app.route('/')
def front():
	return render_templae("TODO: add main page html")
