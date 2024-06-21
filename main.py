from flask import Flask,render_template,url_for

app =Flask( __name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exchange')
def exchange():
    return render_template('exchange.html')



if __name__== "__main__":
    app.run(debug= True)    



