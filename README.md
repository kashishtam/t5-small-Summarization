# Article Summary - T5-small model Text Summarization

## Description
The Article Summary project is an AI-driven tool that uses the T5 (Text-to-Text Transfer Transformer) model to generate concise summaries of news articles and other text. It features a Flask-based API for summarization and a simple web interface for users to input articles and view summaries. 

## Features
- Fine-tuned T5-small (or T5-base) model for high-quality summarization.
- Local Flask API running on `localhost:5001`.
- Local web interface running on `localhost:8000`

## Technologies
- **Google Colab**: For model training and testing with a T4 GPU.
- **Python**: For model training, API, and scripting.
- **PyTorch**: For T5 model inference.
- **Transformers**: Hugging Face library for T5 model and tokenization.
- **Flask**: For the API and CORS support.
- **HTML/CSS/JavaScript**: For the web interface.
- **SentencePiece**: For T5 tokenization.

## Prerequisites
- **Python 3.9+**
- **Node.js** 
- **VS Code** or any text editor 
- **GPU/CPU**: NVIDIA GPU with CUDA (optional, for faster inference) or CPU (slower but works)

## Model Files
Download the fine-tuned T5 model ZIP file [here](https://drive.google.com/file/d/1cqQd6TwE4x0zjzmovrbiVOU1xONTdEkB/view?usp=drive_link).
Unzip it to `./t5_model` in the project folder to use the API.

## Installation

### 1. Clone or Download Repo
If hosted on GitHub, clone it:
```bash
git clone https://github.com/your-username/article-summary.git
cd article-summary
```

### 2. Set up a Virtual Environment

```bash
python3 -m venv summarization_env
source summarization_env/bin/activate  # On MacOS/Linus
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run Flask API 

```bash
python app.py
```

### 2. Run Web Interface 
```bash
serve website locally from different terminal
python -m http.server 8000
```

## Acknowledgements
- Hugging Face for transformers and T5 models.
- Flask team for the web framework.
- Google Colab for T4 GPU training support.
- argilla/news-summary for datasets
