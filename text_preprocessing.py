# Здесь будут собраны все функции для предобработки текста: очистка, токенизация, удаление стоп-слов, лемматизация.
import re
import nltk
import spacy
from nltk.corpus import stopwords
from ntlk.tokenize import word_tokenize 