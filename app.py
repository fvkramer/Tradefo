from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def hello(): 
  url_for('static', filename='style.css')
  return render_template('hello.html', name='Filipp')
#templates have access to   request, session, g, and get_flahsed_messages()
#jinja2

@app.route("/hello")
def what():
  return "WE are in hello"

#converter
# string, int, float, path - (like string but accepts slash), uuid

@app.route('/post/<string:post_id>')
def noError(post_id):
  return "%s" % post_id

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
