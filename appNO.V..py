import nltk
nltk.download('vader_lexicon') # download the lexicon for sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

# create an instance of the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# define a function to classify the sentiment of a user's input
def classify_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return 'positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# define a function to handle the user's input and provide a response
def chatbot():
    while True:
        user_input = input('You: ')
        sentiment = classify_sentiment(user_input)
        if sentiment == 'positive':
            print('Bot: That sounds great!')
        elif sentiment == 'negative':
            print('Bot: I\'m sorry to hear that. Would you like some help resolving the issue?')
            user_response = input('You: ')
            if classify_sentiment(user_response) == 'positive':
                print('Bot: Great! I\'m here to help. Please tell me more about the problem.')
                user_problem = input('You: ')
                #import the trained model with the dataset that classifies the physical or psychological or financial domestic violence problem and proposes solutions
                print('Bot: Thanks for letting me know about the problem. We\'ll work on resolving it as soon as possible.')
            else:
                print('Bot: That\'s okay. Let me know if you change your mind.')
        else:
            print('Bot: Could you please clarify that?')

# start the chatbot with a greeting message
print('Bot: Hi there! How can I help you today?')
#time.sleep(1) # pause for 1 second
chatbot()