from vaderSentiment import vaderSentiment
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix

import csv
import numpy
import pandas
import xlrd

# this is a test variable to make sure script and analyzer are running
# text_for_analysis = {'Comments': ['I love my mother.', 'I hate sticks.', 'There is a dog in my yard.'],
#                      'Sentiment': ['positive', 'negative', 'neutral']}
# comments_dataframe = pandas.DataFrame(text_for_analysis)

# TO DO adjust this so that it reflects the actual form of input
text_for_analysis = '../New_Vader_docs/test_comments_1.xlsx'
comments_read = pandas.read_excel(text_for_analysis)
comments_dataframe = pandas.DataFrame(comments_read)

# split the data into features and labels
X = comments_dataframe['Comments']
y = comments_dataframe['Sentiment']
predictions0 = []
final_scores = []


# this is a function we can export to use later, runs the analyzer and returns the results which we can adjust
def analyze_text(text):
    text_analyzer = vaderSentiment.SentimentIntensityAnalyzer()

    for sentence in text:
        sentiment = ''
        scores = text_analyzer.polarity_scores(sentence)

        if scores['compound'] >= 0:
            sentiment = 'positive'
        elif scores['compound'] < 0:
            sentiment = 'negative'

        final_scores.append({'sentence': sentence, 'scores': scores, 'sentiment': sentiment})
        predictions0.append(sentiment)

    return final_scores, predictions0


analysis, predictions = analyze_text(X)

readout = {'score breakdown': analysis, 'vader_predictions': predictions, 'actual': y}

# this is using the base Vader lexicon which is trained on social media
pandas.DataFrame(readout).to_csv('../Newr_Vader_docs/results_base_1.csv', index=False)

# this is using the modified lexicon
# pandas.DataFrame(readout).to_csv('../Newr_Vader_docs/results_mod_1.csv', index=False)


# evaluate, accept nothing less than 98% :D
print(accuracy_score(y, predictions))
print(confusion_matrix(y, predictions))





