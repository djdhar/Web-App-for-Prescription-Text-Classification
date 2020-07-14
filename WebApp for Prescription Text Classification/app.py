from flask import Flask, redirect, url_for, request, render_template
import os
#import corescript
import core
from datetime import datetime

app = Flask(__name__)

inputt = os.path.join('static', 'input')
app.config['inputt'] = inputt

output = os.path.join('static', 'output')
app.config['output'] = output

@app.route('/')
def index():
    return render_template('index.html', clicked = False)

@app.route('/click', methods =['POST', 'GET'])
def click():
    if request.method == 'POST':
        """
        n = request.form['n']
        if (n == 0) or (n == '') or (n.isnumeric() == False):
            return redirect(url_for('invalidn'))
        """

        file = request.files['nm']
        if file.filename == '':
            return redirect(url_for('nofile'))


        photoid = datetime.now().strftime('%Y%m-%d%H-%M%S')
        
        inputfilename = "saved" + photoid + ".jpg"
        filepath = os.path.join(app.config['inputt'],inputfilename)
        file.save(filepath)
        outputfilename = core.run_(filepath,photoid)
        filepath = os.path.join(app.config['output'], outputfilename)
        return render_template("index.html", clicked = True, filelink = filepath)
        
@app.route('/nofile')
def nofile():
    return render_template('index.html', file=False)

@app.route('/invalidn')
def invalidn():
    return render_template('index.html', inputn=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

