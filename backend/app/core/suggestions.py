import requests
from app.config import config

def get_improvement_suggestions(text):
    api_key = config.API_KEY
    if not api_key:
        raise ValueError("API key not found in config. Please set the API_KEY in the config file.")

    headers = {"Authorization": f"Bearer {api_key}"}
    prompt = (
        f"Please provide detailed suggestions to enhance the quality and readability of the following content. "
        f"Focus on improving user engagement, informativeness, and search engine optimization (SEO). "
        f"Here are the key areas to focus on:\n"
        f"1. Content Enhancement: Provide specific suggestions to improve content clarity and engagement, including an example line with suggestions for improvement.\n"
        f"2. Website-Specific Suggestions: Based on the type of website, give relevant recommendations. For example, if it's a school website, suggest improvements for academic information, usability for parents and students, etc. If it's an e-commerce site, focus on product descriptions, user interface, etc.\n"
        f"3. SEO Recommendations: Suggest relevant keywords and actions to improve the site's search engine ranking.\n"
        f"Keep the suggestions concise and actionable without long paragraphs.\n\n"
        f"Here is the content:\n\n{text}\n\n"
        f"Please provide specific actions to take for each suggestion."
    )

    payload = {
        "prompt": prompt,
        "max_tokens": 200,  # Adjust as needed for more detailed suggestions
        "temperature": 0.5,  # Lower temperature for more focused and coherent suggestions
    }

    try:
        response = requests.post("https://api.cohere.ai/v1/generate", headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        suggestions = response.json().get("generations", [{}])[0].get("text", "")
        return {"suggestions": suggestions}
    except requests.exceptions.HTTPError as http_err:
        raise SystemError(f"HTTP error occurred: {http_err.response.text}")
    except requests.exceptions.RequestException as req_err:
        raise SystemError(f"API request error: {req_err}")
    except IndexError:
        raise SystemError("API response is missing required data.")
    except Exception as e:
        raise SystemError(f"An unexpected error occurred: {e}")