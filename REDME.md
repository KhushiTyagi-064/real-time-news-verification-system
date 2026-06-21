# Real-Time News Verification System Using NLP

## Project Overview

The Real-Time News Verification System Using NLP is a web-based application that helps users verify news claims using real-time information from trusted news sources.

Users can enter a news headline or claim, and the system searches related news articles using NewsAPI. It then compares the user's claim with fetched articles using Natural Language Processing (NLP) and semantic similarity techniques. Based on similarity scores and source credibility, the system predicts whether the news is likely real, likely fake, or requires further verification.

---

## Features

* Real-time news search using NewsAPI
* Keyword extraction from user input
* Semantic similarity analysis using Sentence Transformers
* Source credibility evaluation
* Confidence score generation
* User-friendly Streamlit interface

---

## Technologies Used

* Python
* Streamlit
* NewsAPI
* Sentence Transformers
* Natural Language Processing (NLP)
* Requests Library

---

## Project Workflow

User enters a news headline or claim

↓

Keyword Extraction

↓

Search Related News Articles

↓

Fetch Real-Time News

↓

Semantic Similarity Analysis

↓

Source Credibility Check

↓

Prediction Result

* Likely Real
* Needs Verification
* Likely Fake

---

## Project Structure

real-time-news-verification-system/

│

├── app.py

├── text.py

├── similarity.py

├── credibility.py

├── keyword_extract.py

├── README.md

│

└── requirements.txt

---

## Installation

Install required libraries:

pip install streamlit

pip install requests

pip install sentence-transformers

---

## Run the Project

streamlit run app.py

---

## Future Enhancements

* Google Fact Check API Integration
* Multi-language Support
* Image Verification
* Browser Extension
* AI-powered Explanation System

---

## Author

Khushi Tyagi

B.Tech CSE (AI & ML)

COER University
