import string
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class TextAnalyzer:
    def __init__(self, text_file, emotions_file):
        self.text_file = text_file
        self.emotions_file = emotions_file
        self.text = self.read_text()
        self.stop_words = self.get_stop_words()
        self.cleaned_text = self.clean_text()
        self.tokenized_words = self.tokenize_text()
        self.final_words = self.remove_stop_words()
        self.emotion_list = self.analyze_emotions()
        self.emotion_counts = self.count_emotions()

    def read_text(self):
        with open(self.text_file, encoding="utf-8") as file:
            return file.read()

    def get_stop_words(self):
        return ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    def clean_text(self):
        lower_case = self.text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        return cleaned_text

    def tokenize_text(self):
        return self.cleaned_text.split()

    def remove_stop_words(self):
        return [word for word in self.tokenized_words if word not in self.stop_words]

    def analyze_emotions(self):
        emotion_list = []
        with open(self.emotions_file, 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')

                if word in self.final_words:
                    emotion_list.append(emotion)
        return emotion_list

    def count_emotions(self):
        return Counter(self.emotion_list)

    def plot_emotions(self):
        fig, ax = plt.subplots(1, 3, figsize=(18, 6))

        # Bar Chart
        ax[0].bar(self.emotion_counts.keys(), self.emotion_counts.values(), color='skyblue')
        ax[0].set_title('Emotion Counts')
        ax[0].set_ylabel('Count')
        ax[0].set_xlabel('Emotions')

        # Histogram
        ax[1].hist(self.emotion_list, bins=len(self.emotion_counts), edgecolor='black', color='lightgreen')
        ax[1].set_title('Emotion Histogram')
        ax[1].set_ylabel('Frequency')
        ax[1].set_xlabel('Emotions')

        # Pie Chart
        ax[2].pie(self.emotion_counts.values(), labels=self.emotion_counts.keys(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(self.emotion_counts))))
        ax[2].set_title('Emotion Proportions')

        fig.autofmt_xdate()
        plt.tight_layout()
        plt.savefig('emotions_plot.png')
        plt.show()

    def generate_word_cloud(self):
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(self.final_words))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Final Words')
        plt.savefig('word_cloud.png')
        plt.show()

