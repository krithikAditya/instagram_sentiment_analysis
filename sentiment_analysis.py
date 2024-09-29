# sentiment_analysis.py

import os
import instaloader
import pytesseract
from PIL import Image
import nltk
from nltk.tokenize import word_tokenize
from transformers import pipeline

# Disable symlinks warning
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Set up Tesseract path (update this path for your system)
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Constants
SESSION_FILE = 'srmproject2'
POST_LIMIT = 5

# Step 1: Instagram Data Collection
def collect_instagram_data(username):
    L = instaloader.Instaloader()

    try:
        L.load_session_from_file(SESSION_FILE)
    except FileNotFoundError:
        print("Session file not found. Please log in manually using the instaloader CLI.")
        exit()
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection Exception: {e}")
        exit()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print(f"Profile '{profile.username}' found with {profile.mediacount} posts.")
    except Exception as e:
        print("Failed to find the target profile:", e)
        return None

    post_directory = f"{profile.username}_posts"
    os.makedirs(post_directory, exist_ok=True)

    print("Starting download of posts...")
    post_count = 0
    for post in profile.get_posts():
        print(f"Downloading post: {post.url}")
        L.download_post(post, target=post_directory)
        post_count += 1
        if post_count >= POST_LIMIT:
            break

    return post_directory

# Step 2: Text Extraction from Images
def extract_text_from_images(image_dir):
    texts = []
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            image_path = os.path.join(image_dir, filename)
            print(f"Processing image: {image_path}")
            try:
                text = pytesseract.image_to_string(Image.open(image_path))
                print(f"Extracted text: {text}")
                texts.append(text)
            except Exception as e:
                print(f"Failed to process image {image_path}: {e}")
    return texts

# Step 3: Text Extraction from Descriptions
def extract_text_from_descriptions(username):
    L = instaloader.Instaloader()

    try:
        L.load_session_from_file(SESSION_FILE)
    except FileNotFoundError:
        print("Session file not found. Please log in manually using the instaloader CLI.")
        exit()
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection Exception: {e}")
        exit()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print(f"Profile '{profile.username}' found with {profile.mediacount} posts.")
    except Exception as e:
        print("Failed to find the target profile:", e)
        return None

    descriptions = []
    post_count = 0
    for post in profile.get_posts():
        if post.caption:
            descriptions.append(post.caption)
            print(f"Extracted description: {post.caption}")
        post_count += 1
        if post_count >= POST_LIMIT:
            break

    return descriptions

# Step 4: Data Processing
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum()]
    return ' '.join(filtered_tokens)

def combine_text_data(image_texts, description_texts):
    all_texts = image_texts + description_texts
    preprocessed_texts = [preprocess_text(text) for text in all_texts]
    return preprocessed_texts

# Step 5: Sentiment and Emotion Analysis
def analyze_sentiment(texts):
    sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
    sentiment_results = [sentiment_analyzer(text) for text in texts]
    return sentiment_results

def analyze_emotions(sentiments):
    emotion_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    for result in sentiments:
        label = result[0]['label'].lower()
        if label not in emotion_counts:
            emotion_counts[label] = 0
        emotion_counts[label] += 1
    total = len(sentiments)
    if total == 0:
        print("No sentiments analyzed. Check your text extraction and preprocessing steps.")
        return {}
    emotion_percentage = {k: (v / total) * 100 for k, v in emotion_counts.items()}
    return emotion_percentage
