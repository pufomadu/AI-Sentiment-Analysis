import matplotlib.pyplot as plt



def make_plot(sentiments: list) -> list:
    """
    Takes a list of sentiment labels and generates a bar chart to visualize the frequency of each sentiment: positive, neutral, negative, and irrelevant.

    The chart is saved as 'images/sentiment_plot.png'. This function does not return anything.

    The function returns the sentiment labels and their corresponding counts.
    
    Args: 
        sentiments (list): A list of strings representing sentiment labels (e.g., ["positive", "negative", "neutral"])

    Returns: 
        None, this function is not required to return any values.
    """
    # Initialize counts for all expected sentiment categories
    sentiment_counts = {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "irrelevant": 0
    }

     # Count each sentiment 
    for sentiment in sentiments:
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1

    #Data for plotting
    categories = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())


    # Create a bar chart to visualize the sentiment distribution
    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts) 
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Distribution")
    plt.tight_layout()

    # Save the chart to the images folder
    plt.savefig("images/sentiment_chart.png")
    plt.close()

