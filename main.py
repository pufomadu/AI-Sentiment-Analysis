from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Function to run the sentiment analysis pipeline.

    This function takes a file path to a JSON file containing customer reviews, 
    extracts the reviews, analyzes their sentiment using the OpenAI API,
    and visualizes the frequency of each sentiment using a bar chart.

    Args:
        filepath (str): Path to the JSON file containing customer reviews.

    Returns:
        list: A list of sentiment labels corresponding to each review.
    """

    # open the json object
    with open(filepath, "r") as file:
        data = json.load(file)

    # extract the reviews from the json file
    reviews = data.get("results", [])

    if not isinstance(reviews, list) or not reviews:
        return []

    for review in reviews:
        if not isinstance(review, str):
            return []

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)
    
    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
