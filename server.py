from flask import Flask

app = Flask(__name__)

@app.route('/<bs>')
def rev(bs):
	print bs
	return 'Bs is %s' %bs

if __name__ == '__main__':
	app.debug = True
	# app.register_blueprint(app, url_prefix='/metro')
	#app.register_blueprint(app, url_prefix='/')
	app.run(host='0.0.0.0')
