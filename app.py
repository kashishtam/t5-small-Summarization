from flask import Flask, request, jsonify
import torch
from flask_cors import CORS
from transformers import T5ForConditionalGeneration, T5Tokenizer
import os

app = Flask(__name__)
CORS(app) # Allow all origins (fix for CORS blocking)

model_path = "./t5_model/t5_summarization_model/final"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

def generate_summary(article_text, max_length=70, length_penalty=2.5, num_beams=2):
    inputs = tokenizer("summarize: " + article_text , max_length=512, truncation=True, padding="max_length", return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)
    summary_ids = model.generate(input_ids, attention_mask=attention_mask, max_length=max_length, min_length=15, length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary[0].upper() + summary[1:] if summary else ""

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    article_text = data.get('article', '')
    if not article_text:
        return jsonify({'error': 'No article text provided'}), 400
    summary = generate_summary(article_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))