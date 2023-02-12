"""Web Translator Service using Flask"""
from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request

app = Flask("Web Translator")


@app.route("/englishToFrench")
def english_to_french_endpoint():
    """Translate an input text in English to French"""
    text_to_translate = request.args.get('textToTranslate')
    if text_to_translate is None:
        return "Error: English text not provided", 400
    french_text = english_to_french(text_to_translate)
    return french_text


@app.route("/frenchToEnglish")
def french_to_english_endpoint():
    """Translate an input text in French to English"""
    text_to_translate = request.args.get('textToTranslate')
    if text_to_translate is None:
        return "Error: French text not provided", 400
    english_text = french_to_english(text_to_translate)
    return english_text


@app.route("/")
def renderIndexPage():
    """Render template"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
