from flask import Flask, render_template, request, redirect, url_for, session
from heun_method import heun_method

app = Flask(__name__)

# SECRET KEY FOR SESSION
app.secret_key = "heun_secret_key"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/examples')
def examples():
    return render_template('example.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    # SHOW SAVED DATA
    if request.method == 'GET':

        return render_template(
            'calculator.html',
            result=session.pop('result', None),
            steps=session.pop('steps', []),

            equation=session.pop('equation', ''),
            x0=session.pop('x0', ''),
            y0=session.pop('y0', ''),
            h=session.pop('h', ''),
            target=session.pop('target', '')
        )

    # FORM SUBMISSION
    equation = request.form['equation']

    x0 = request.form['x0']
    y0 = request.form['y0']
    h = request.form['h']
    target = request.form['target']

    # COMPUTE HEUN METHOD
    result, steps = heun_method(
        equation,
        float(x0),
        float(y0),
        float(h),
        float(target)
    )

    # SAVE RESULT
    session['result'] = result
    session['steps'] = steps

    # SAVE INPUTS
    session['equation'] = equation
    session['x0'] = x0
    session['y0'] = y0
    session['h'] = h
    session['target'] = target

    # REDIRECT
    return redirect(url_for('calculator'))


if __name__ == '__main__':
    app.run()
    