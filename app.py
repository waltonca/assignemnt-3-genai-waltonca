from flask import Flask, request, render_template
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Load MarianMT model and tokenizer for Chinese to English translation
model_name = "Helsinki-NLP/opus-mt-zh-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text_input"]
        if text:
            # Translate Chinese text to English
            translated = translate_text(text)
            return render_template("index.html", original=text, translated=translated)
        else:
            return render_template("index.html", error="Please provide some text.")

    return render_template("index.html")

def translate_text(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    
    # Translate the text
    translated_tokens = model.generate(**inputs)
    
    # Decode the translated tokens to a string
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    
    return translated_text

if __name__ == "__main__":
    app.run(debug=True)