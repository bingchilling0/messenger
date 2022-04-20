from flask import Flask, request, render_template
from time import localtime

all_messages = []
app = Flask(__name__)


@app.route("/")
def index_page():
    return "cum"


@app.route("/get_messages")
def get_message():
    return {"messages": all_messages}


@app.route("/chat")
def display_chat():
    return render_template("form.html")


@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    return ""


def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": str(localtime().tm_hour) + ":" + str(localtime().tm_min)
    }

    if len(new_message["sender"]) in range(3, 101) and len(new_message["text"]) in range(1, 3001):
        all_messages.append(new_message)


app.run()
