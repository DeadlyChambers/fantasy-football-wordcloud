import wordcloud
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

# Load the chat text from the file
with open('_chat.txt', 'r') as f:
    lines = f.readlines()
 
last_10k_lines = lines[-1000:]
chat_text = '\n'.join(last_10k_lines)

# Split each line by ':' and take the last part (the message text)
# Also, remove any leading or trailing whitespace
chat_text = '\n'.join(line.split(':', 3)[-1].strip() for line in chat_text.split('\n'))
#nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))

ignore_words = english_stopwords.union(['justin', 'ethan', 'omitted', 'tony', 'joe', 'carissa', 'matt', 'david', 'dykstra', 'shane', "don't", 'image',  "it's", 'gif', 'message', 'a', 'an', 'the', 'and', 'is', 'in', 'on', 'at', 'by', 'with', 'from',
    'to', 'of', 'no', 'not', 'but', 'or', 'be', 'as', 'for', 'that', 'this',
    'these', 'those', 'are', 'was', 'were', 'been', 'have', 'has', 'had',
    'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can', 'could', 'oh','wow','gonna', 'still', 'good','game',
    'may', 'might', 'must', 'i', 'me', 'my', 'mine', 'you', 'your', 'yours',
    'he', 'him', 'his', 'she', 'her', 'hers',  'its', 'we', 'us', 'our', 'know', 'don', 't', 'too', 'then', 'who', 'sean', 
    'ours', 'they', 'them', 'their', 'theirs', 'just', 'yeah', 'think', 'lol', 's', 'get', 'all', 'like', 'if', 'out', 'want', 'when', 'don\'t', 'so', 'didn\'t', 'yeah', 'said', 'edited', 'one', 'there', 'because', 'what', 'when', 'how', 'why','get', 'got', 'need', 'up', 'm', 'I\'m', 'some', 'time','maybe'])

# Generate the word cloud
wordcloud = WordCloud(stopwords=ignore_words).generate(chat_text)
# Display the word cloud
# wordcloud.to_image()

# Save the word cloud as a PNG file
wordcloud.to_file('wordcloud.png')
