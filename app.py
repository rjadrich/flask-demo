from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/ticker_input')

@app.route('/ticker_input', methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('ticker_input.html')
  else:
    app.vars['ticker'] = request.form['ticker']
    app.vars['ticker_options'] = request.form.getlist('ticker_options')

    message = 'id chosen: %s options selected:' % app.vars['ticker']
    for entry in app.vars['ticker_options']:
        message = message + " " + entry

    return message

if __name__ == '__main__':
  app.run(port=33507)
