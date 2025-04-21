#Import the necessary libraries (the OpenAI client to interact with the OpenAI API)
import os
from openai import OpenAI

#Initialize the OpenAI client
client = OpenAI()

def get_sentiment(text: list) -> list:
    """
    Analyze the sentiment of a list of text strings using OpenAI's gpt-4o-mini model.

    Each string is categorized as positive, neutral, negative, or irrelevant.

    The function returns a list of sentiments corresponding to each input string.

    Args:
        text (list): A list of strings to analyze

    Returns:
        list: A list of sentiments corresponding to each input string

    Note:
        If the input list is empty, the function returns an error message.
            "Wrong input. Text must be an array of strings."
    """
    # Input validation: Check if the input is a list and not empty
    
    if not isinstance(text, list) or not text:
        return "Wrong input. text must be an array of strings."
    for item in text:
        if not isinstance(item, str):
            return "Wrong input. text must be an array of strings."

    # Define the system prompt for the OpenAI API that instructs the model how to behave
    system_prompt = """ 
    
    You are a sentiment analysis expert.
    
    # Instructions:
    You will be given a list of customer reviews. For each review, classify each one as either positive, neutral, negative, or irrelevant.

    Finally, you will return exactly one word per review, all lowercase and in the same order as the input reviews.
    
    Use one word per line only. Do not add any explanations or additional information, just the sentiment classification.

    # Examples:
    if your input file contains the following array of reviews:
        ```
        [
        "this ring smells weird, don't recomend",
        "I love this ring, I use it all the time when working out.",
        "its a ring"
        ]
        ```
    Your program would output the following list of labels:
    ```
        ["negative", "positive", "positive", "neutral", "irrelevant", "negative"]
    ``` 
    """

   # Construct the user prompt with the input reviews   

    prompt = f"""
    For each line of text in the string below, please categorize the review as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.

    {"\\n".join(text)}
    """
    
    # Call the OpenAI API to get the response from the model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and clean the response text from the API response
    response_text = response.choices[0].message.content.strip()

    # Process each line of the model's response by stripping whitespace, filtering out blanks, converting to lowercase, and storing the cleaned sentiments
    sentiments = []
    for line in response_text.splitlines():
        cleaned_line = line.strip().lower()
        if cleaned_line:  # Check if the line is not empty
            sentiments.append(cleaned_line)

    return sentiments




