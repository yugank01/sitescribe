
# Backend - Site Scraping & Sentiment Analysis API

## Overview
This project is a backend API built using **FastAPI** that allows users to scrape content from a given URL, perform sentiment analysis on the scraped text, and provide improvement suggestions based on the text data. The API exposes the following endpoints:

- `/scrape/` - Scrapes a given URL and extracts headlines and paragraphs.
- `/analyze/` - Analyzes the sentiment of the scraped data.
- `/suggestions/` - Provides suggestions to improve the scraped content.

## Requirements

Before running the application, make sure you have the following installed:

- Python 3.7+
- `pip` (Python package installer)

### Step 1: Clone the Repository


git clone <repository-url>
cd <repository-directory>


### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It’s recommended to set up a virtual environment to keep dependencies isolated.


# For Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate


### Step 3: Install Requirements

Install the required dependencies using `pip`.


pip install -r requirements.txt


This will install the following dependencies:
- `fastapi` - The web framework for building APIs.
- `uvicorn` - ASGI server for serving the FastAPI app.
- `beautifulsoup4` - For web scraping.
- `requests` - To make HTTP requests for scraping.
- `transformers` - For sentiment analysis (Huggingface models).
- `scikit-learn` - Machine learning library used in sentiment analysis.

### Step 4: Run the FastAPI Server

To start the backend server, use the following command:

uvicorn app.main:app --reload


The server will run locally at `http://127.0.0.1:8000`. You can now test the APIs using tools like **Postman** or **curl**.

---

## API Endpoints

### 1. `/scrape/` - Scrape a given URL

- **Method**: `POST`
- **URL**: `/scrape/`
- **Request Body**: 
    ```json
    {
        "url": "https://example.com"
    }
    ```
    - `url`: The URL of the website you want to scrape.

- **Response**: A JSON object containing scraped data:
    ```json
    {
        "data": {
            "headlines": ["Headline 1", "Headline 2"],
            "paragraphs": ["Paragraph 1", "Paragraph 2"]
        }
    }
    ```
    - `headlines`: An array of extracted headlines from the page.
    - `paragraphs`: An array of extracted paragraphs from the page.

---

### 2. `/analyze/` - Analyze Sentiment of Scraped Data

- **Method**: `POST`
- **URL**: `/analyze/`
- **Request Body**:
    ```json
    {
        "data": {
            "headlines": ["Headline 1", "Headline 2"],
            "paragraphs": ["Paragraph 1", "Paragraph 2"]
        }
    }
    ```

- **Response**: Sentiment analysis result:
    ```json
    {
        "sentiment": "NEGATIVE",
        "confidence": 0.9973322153091431
    }
    ```
    - `sentiment`: The sentiment of the text (e.g., "POSITIVE", "NEGATIVE", "NEUTRAL").
    - `confidence`: The confidence score of the sentiment prediction.

---

### 3. `/suggestions/` - Get Suggestions for Improvement

- **Method**: `POST`
- **URL**: `/suggestions/`
- **Request Body**:
    ```json
    {
        "data": {
            "headlines": ["Headline 1", "Headline 2"],
            "paragraphs": ["Paragraph 1", "Paragraph 2"]
        }
    }
    ```

- **Response**: Suggestions for improving the scraped content:
    ```json
    [
        "Suggestion 1",
        "Suggestion 2"
    ]
    ```
    - An array of strings containing improvement suggestions.

---

## Troubleshooting

- **Error Handling**: If there’s an issue with scraping or analyzing the content, the API will return a 500 status code with an error message. Be sure the URL you're passing is valid and accessible.
  
  Example of error response:
  ```json
  {
      "detail": "An error occurred: Invalid URL"
  }
  ```

- **CORS Issues**: If you encounter CORS issues while using the frontend, ensure that the `allow_origins` in the FastAPI settings allow requests from your frontend.

---

## Example Workflow

1. **Scrape Data**:  
   Send a `POST` request to `/scrape/` with the URL of the page you want to scrape.
   
   Example request:
   ```bash
   curl -X 'POST' \
   'http://127.0.0.1:8000/scrape/' \
   -H 'Content-Type: application/json' \
   -d '{
       "url": "https://example.com"
   }'
   ```
   Response:
   ```json
   {
       "data": {
           "headlines": ["Example Headline 1", "Example Headline 2"],
           "paragraphs": ["This is a paragraph", "Another paragraph."]
       }
   }
   ```

2. **Analyze Sentiment**:  
   Send the scraped data to the `/analyze/` endpoint for sentiment analysis.
   
   Example request:
   ```bash
   curl -X 'POST' \
   'http://127.0.0.1:8000/analyze/' \
   -H 'Content-Type: application/json' \
   -d '{
       "data": {
           "headlines": ["Example Headline 1", "Example Headline 2"],
           "paragraphs": ["This is a paragraph", "Another paragraph."]
       }
   }'
   ```
   Example response:
   ```json
   {
       "sentiment": "NEGATIVE",
       "confidence": 0.9973322153091431
   }
   ```

3. **Get Suggestions**:  
   Send the scraped data to the `/suggestions/` endpoint to get content improvement suggestions.
   
   Example request:
   ```bash
   curl -X 'POST' \
   'http://127.0.0.1:8000/suggestions/' \
   -H 'Content-Type: application/json' \
   -d '{
       "data": {
           "headlines": ["Example Headline 1", "Example Headline 2"],
           "paragraphs": ["This is a paragraph", "Another paragraph."]
       }
   }'
   ```
   Example response:
   ```json
   [
       "Consider simplifying the language.",
       "Add more detail to the second paragraph."
   ]
   ```

---
```

