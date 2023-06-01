from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from cleaner import clean_corpus

app = Flask(__name__)

CORPUS_FILE = "chat.txt"

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(english_bot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
