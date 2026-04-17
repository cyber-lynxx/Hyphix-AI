from flask import Flask, render_template, redirect, url_for
from jinja2.exceptions import TemplateNotFound
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO()
socketio.init_app(app)

@app.route("/")
def route_index():
  return redirect("/page/index")

@app.route("/page/<name>")
def route(name):
  try:
    result = render_template(f"{name}.html")
  except TemplateNotFound:
    result = render_template("page_not_found.html")
  return result

@app.errorhandler(404)
def page_not_found(e):
  return render_template("page_not_found.html")

@socketio.on("message")
def handle_message(data):
  print(data)

if __name__ == "__main__":
  socketio.run(app, debug = True, host = "0.0.0.0", port = 8080)
