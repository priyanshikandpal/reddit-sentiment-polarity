import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from textblob import TextBlob
import seaborn as sns
import os
from wordcloud import WordCloud  

def barGraphic(sentiments):
    num_positive = len([s for s in sentiments if s > 0])
    num_negative = len([s for s in sentiments if s < 0])
    num_neutral = len([s for s in sentiments if s == 0])

    labels = ["Positive", "Negative", "Neutral"]
    counts = [num_positive, num_negative, num_neutral]

    plt.bar(labels, counts, color=["green", "red", "gray"])
    plt.title("Sentiment Distribution of Comments")
    plt.ylabel("Number of Comments")
    plt.grid(axis="y")
    plt.savefig('static/graphs/bar_graphic.png')
    plt.close()


def dispersionGraphic(sentiments, texts):
    text_lengths = [len(text) for text in texts]
    plt.scatter(text_lengths, sentiments, alpha=0.7, color="purple")
    plt.title("Sentiment vs. Text Length\n(Example: Short comments like 'Great!' vs. long reviews)")
    plt.xlabel("Text Length")
    plt.ylabel("Sentiment Polarity (-1 to 1)")
    plt.grid(True)
    plt.savefig('static/graphs/dispersion_graphic.png')
    plt.close()

def pizzaGraphic(sentiments):
    num_positive = len([sentiment for sentiment in sentiments if sentiment > 0])
    num_negative = len([sentiment for sentiment in sentiments if sentiment < 0])
    num_neutral = len([sentiment for sentiment in sentiments if sentiment == 0])
    labels = ["Positive", "Negative", "Neutral"]
    sizes = [num_positive, num_negative, num_neutral]
    colors = ["green", "red", "gray"]
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title("Distribution of Sentiments\n(Example: Comments classified into positive, negative, or neutral)")
    plt.savefig('static/graphs/pizza_graphic.png')
    plt.close()

def warmthGraphic(key_words, texts):
    # Ensure all elements in texts are strings
    texts = [str(text) for text in texts]

    # Create a dictionary to count keyword occurrences
    keyword_counts = {keyword: 0 for keyword in key_words}
    
    # Count occurrences of each keyword in the texts
    for text in texts:
        for keyword in key_words:
            keyword_counts[keyword] += text.lower().count(keyword.lower())  # Case-insensitive match
    
    # Check if all counts are zero (no matches found)
    if all(count == 0 for count in keyword_counts.values()):
        print("Warning: No matches found for the provided keywords in the comments.")

    # Prepare data for the heatmap
    keywords = list(keyword_counts.keys())
    counts = list(keyword_counts.values())
    
    # Generate the heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap([counts], annot=True, fmt="d", xticklabels=keywords, yticklabels=["Frequency"], cmap="YlGnBu")
    plt.title("Keyword Frequency Heatmap")
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.savefig('static/graphs/warmth_graphic.png')  # Save the heatmap to a file
    plt.close()

def histogram(sentiments):
    plt.hist(sentiments, bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribution of Sentiment in Comments\n(Example: How sentiments are distributed across comments)")
    plt.xlabel("Sentiment Polarity (-1 to 1)")
    plt.ylabel("Number of Comments")
    plt.grid(axis="y")
    plt.savefig('static/graphs/histogram.png')
    plt.close()

def lineGraphic(sentiments):
    plt.plot(sentiments, marker="o", linestyle="-", color="blue")
    plt.title("Variation of Sentiment in Comments\n(Example: Sequential sentiment changes across comments)")
    plt.xlabel("Comment Index")
    plt.ylabel("Sentiment Polarity (-1 to 1)")
    plt.grid(True)
    plt.savefig('static/graphs/line_graphic.png')
    plt.close()

def wordCloudGraphic(texts):
    # Combine all texts into a single string
    combined_text = " ".join(texts)
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(combined_text)
    
    # Plot and save the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Comments")
    plt.savefig('static/graphs/word_cloud.png')  # Save the word cloud to a file
    plt.close()

def generate_graphs(sentiments, texts):
    # Ensure the directory exists
    if not os.path.exists('static/graphs'):
        os.makedirs('static/graphs')

    # Generate individual graphs
    barGraphic(sentiments)
    dispersionGraphic(sentiments, texts)
    pizzaGraphic(sentiments)
    warmthGraphic(['example_keyword'], texts)  # Replace with actual keywords
    histogram(sentiments)
    lineGraphic(sentiments)
    wordCloudGraphic(texts)  # Generate the word cloud

    # Generate a PDF containing all the graphs
    with PdfPages('static/graphs/sentiment_analysis.pdf') as pdf:
        for graph in ['bar_graphic.png', 'dispersion_graphic.png', 'pizza_graphic.png', 'warmth_graphic.png', 'histogram.png', 'line_graphic.png', 'word_cloud.png']:
            img = plt.imread(f'static/graphs/{graph}')
            plt.imshow(img)
            plt.axis('off')
            pdf.savefig()
            plt.close()