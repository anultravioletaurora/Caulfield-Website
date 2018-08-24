from flask import Flask, render_template

app = Flask(__name__)


# Takes user to the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# Takes user to about me
@app.route('/about')
def about():
    return render_template('about.html')


# Takes user to blog
@app.route('/blog')
def blog():
    return render_template('blog.html')


# Takes user to photos page
@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/fontawesomeicon/<iconname>')
def geticon(iconname):
    return '<i class="fas fa-' + iconname + '</i>'


if __name__ == '__main__':
    app.run(debug=True)
