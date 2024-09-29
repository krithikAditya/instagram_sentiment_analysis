## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Instagram Sentiment & Emotion Analysis

This project is a web-based application designed to analyze the sentiment and emotions of Instagram users by extracting text from images and post descriptions. It utilizes OCR (Optical Character Recognition) for image text extraction, Instaloader for Instagram data collection, and Natural Language Processing (NLP) models to determine the sentiment and emotions within the posts.

## Features

- **Instagram Data Collection**: Downloads up to 5 recent posts from a specified Instagram profile.
- **Text Extraction**: Uses Tesseract OCR to extract text from images posted on Instagram.
- **Sentiment Analysis**: Leverages a pre-trained NLP model to analyze the sentiment (positive, negative, or neutral) in the extracted text.
- **Emotion Detection**: Categorizes emotions based on the sentiment and provides a summary of the user's emotional state.
- **User-Friendly Interface**: Input an Instagram username and receive emotion percentages and an easy-to-understand summary indicating the user’s emotional health.

## How It Works

1. **Data Collection**: The app fetches posts and descriptions from a specified Instagram profile using Instaloader.
2. **Text Extraction**: Extracts any text from the post images and captions.
3. **Sentiment Analysis**: Analyzes the extracted text to classify it as positive, negative, or neutral.
4. **Emotion Detection**: Calculates the percentages of positive, negative, and neutral emotions in the posts.
5. **Results**: Displays a user-friendly summary indicating whether the user is happy, neutral, or potentially experiencing depression.

## Installation Instructions

### 1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

---------------------------------------------------------------------
Set Up a Virtual Environment (Optional but Recommended): 

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
---------------------------------------------------------------------
Install Dependencies:

pip install -r requirements.txt
--------------------------------------------------------------------
 Set Up Tesseract OCR:
Download and install Tesseract OCR.
Update the tesseract_cmd path in the sentiment_analysis.py file to match your system's Tesseract installation path.
5. Log In to Instagram:
Use the Instaloader CLI to log in and generate a session file by running instaloader in your terminal.
Save the generated session file in the project root directory under the name srmproject2. ( use your own instagram id and password this will be disbled)
--------------------------------------------------------------------
Project Structure
├── app.py                 # Main Flask app for the web interface
├── sentiment_analysis.py   # Handles Instagram data collection and sentiment analysis
├── requirements.txt        # Lists all dependencies
├── templates/
│   ├── index.html          # Input form for the Instagram username
│   └── result.html         # Displays sentiment and emotion analysis results
├── static/
│   └── style.css           # CSS styling for the web interface
└── README.md               # This readme file
------------------------------------------------------------------------
Usage
On the home page (/), enter an Instagram username in the provided input field.
Click on "Analyze" to initiate the sentiment and emotion analysis process.
After the analysis, view the results, which include the sentiment percentages and a summary indicating the user's emotional state (e.g., happy, slightly happy, neutral, or experiencing depression).
Requirements
Python 3.x
Flask
Instaloader
Tesseract OCR
HuggingFace Transformers (for sentiment analysis)
-------------------------------------------------------------------------------
Contributing
If you'd like to contribute to the project, feel free to fork the repository and submit a pull request with your improvements. Contributions are always welcome!
--------------------------------------------------------------------------------------------
License
This project is licensed under the MIT License - see the LICENSE file for details.

### How to Use This `README.md`:
- **Repository Name**: Replace `your-username` and `your-repo-name` in the cloning section with the appropriate GitHub repository details.
- **Tesseract Path**: Update the path to Tesseract OCR if you want to provide more detailed instructions specific to users.
- **Session File**: Adjust the name of the session file (`srmproject2`) if you've named it differently.

This README should give users everything they need to understand, install, and run your project.

