import string
from collections import Counter
import matplotlib.pyplot as plt

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
        emotion_counts = self.count_emotions()
        fig, ax1 = plt.subplots()
        ax1.bar(emotion_counts.keys(), emotion_counts.values())
        fig.autofmt_xdate()
        plt.savefig('graph.png')
        plt.show()
