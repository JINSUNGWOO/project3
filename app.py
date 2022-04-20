from crypt import methods
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main_page():
    if methods == 'POST':
        output = request.form.to_dict()
        team_name = output["keyword1"]
        
        return render_template('gamesquad.html')
    else:
        return render_template('index.html')


@app.route('/fixture')
def fixture_page():
    return render_template('rankingtable.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('my_pick.html')


@app.route('/<string:pick>')
def my_pick(pick):
    mp = render_template('my_pick.html', content= pick)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)