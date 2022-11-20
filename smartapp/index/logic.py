import string
import nltk
import requests
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from bs4 import BeautifulSoup


def punctuation_removal(text):
    for character in text:
        if character in string.punctuation:
            text = text.replace(character, "")
    return text


def text_upper(text):
    return text.upper()


def text_lower(text):
    return text.lower()


def remove_new_line(text):
    text = ''.join(text.splitlines())
    return text


def remove_extra_space(text):     # removes duplicate whitespaces and newline characters
    text = ' '.join(text.split())
    return text


def count_characters(text):
    text = len(text)
    return text


def spell(text):
    b = TextBlob(text)
    corrected_text = b.correct()
    return corrected_text


def wiki(text):
    summary = requests.get('https://en.wikipedia.org/wiki/'+text)
    soup = BeautifulSoup(summary.text, 'lxml')
    return soup.get_text()


def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = []

    for w in word_tokens:
        if w.lower() not in stop_words:
            filtered_sentence.append(w)
    text = ' '.join(filtered_sentence)
    return text
