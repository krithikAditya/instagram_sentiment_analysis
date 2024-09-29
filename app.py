from flask import Flask, render_template, request
from sentiment_analysis import collect_instagram_data, extract_text_from_images, extract_text_from_descriptions, combine_text_data, analyze_sentiment, analyze_emotions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.form['username']

    # Collect data and perform analysis
    post_directory = collect_instagram_data(username)
    if not post_directory:
        return render_template('result.html', result={"error": f"Profile '{username}' found with 0 posts."})

    image_texts = extract_text_from_images(post_directory)
    description_texts = extract_text_from_descriptions(username)
    preprocessed_texts = combine_text_data(image_texts, description_texts)

    if not preprocessed_texts:
        return render_template('result.html', result={"error": f"Profile '{username}' found with no text data to analyze."})

    sentiments = analyze_sentiment(preprocessed_texts)
    emotion_percentages = analyze_emotions(sentiments)

    result = {
        'positive': emotion_percentages.get('positive', 0),
        'negative': emotion_percentages.get('negative', 0),
        'neutral': emotion_percentages.get('neutral', 0)
    }

    # Determine the summary based on the sentiment percentages
    if result['negative'] > 50:
        summary = "The user may be experiencing significant depression."
    elif result['negative'] > 30:
        summary = "The user may be experiencing mild depression."
    elif result['positive'] > 50:
        summary = "The user seems happy."
    elif result['positive'] > 30:
        summary = "The user seems slightly happy."
    else:
        summary = "The user's emotions are quite neutral."

    return render_template('result.html', result=result, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
