# ScamFish

ScamFish is a Chrome extension that detects potential spam emails in Gmail using an ML model trained on the Apache SpamAssasin. 

## Features

- Detects potential scam emails in Gmail.
- Uses a FastAPI backend for processing email content.
- Chrome extension for easy access and usage.

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- Google Chrome

### Manual Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/abelosbert06/SpamFish
    cd SpamFish
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the FastAPI server**:

    ```sh
    uvicorn server:app --reload
    ```

5. **Load the Chrome extension**:

    - Open Chrome and go to `chrome://extensions/`.
    - Enable "Developer mode".
    - Click "Load unpacked" and select the `extension` directory.

6. **Use the extension**:

    - Open Gmail and select an email.
    - Click the SpamFish extension icon and click "Check Email" to detect potential scam emails.

## Machine Learning Model
The machine learning model is trained using logistic regression to predict if an email is spam or not.

**Dataset**:

This extention uses the version of Apache SpamAssasin Public Corupus contributed by the creators of the Bayesian spam filter SpamAssassin. This version has the various csv files (spam and ham datasets) combined into a single dataset.


**Apache SpamAssasin Public Corpus**: https://spamassassin.apache.org/old/publiccorpus/

**Combined Dataset**: https://www.kaggle.com/datasets/bertvankeulen/spamassassin-spam


## Roadmap

- Additional browser support

- Add more variables in the spam detection process (email address, time of day, etc)


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)  License.


## Acknowledgements

 - [Kaggle Dataset](https://www.kaggle.com/datasets/bertvankeulen/spamassassin-spam)
 - [Namrata Mane's notebook on working with the SpamAssasin Dataset](https://www.kaggle.com/code/namrata3632/email-spam-detection)


