from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/ticker_input')

@app.route('/ticker_input')
def index():
  return render_template('ticker_input.html')

if __name__ == '__main__':
  app.run(port=33507)
