from Lapp import TextAnalyzer

# Instantiate the TextAnalyzer class
text_file = 'read.txt'
emotions_file = 'emotions.txt'
analyzer = TextAnalyzer(text_file, emotions_file)

# Print emotion list and their counts
print(analyzer.emotion_list)
emotion_counts = analyzer.count_emotions()
print(emotion_counts)

# Plot the emotions
analyzer.plot_emotions()
