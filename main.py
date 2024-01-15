from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    name = request.form.get('name')
    return f"Hello, {name}!"
  return render_template('index.html')

@app.route('/welcome')
def page2():
  return render_template('welcome.html')

@app.route('/creativity')
def page3():
  return render_template('creativity.html')

@app.route('/problemsolving')
def page4():
  return render_template('problemsolving.html')

@app.route('/comms')
def page5():
  return render_template('comms.html')

@app.route('/critical')
def page6():
  return render_template('critical.html')
  
app.run(host='0.0.0.0', port=81)

