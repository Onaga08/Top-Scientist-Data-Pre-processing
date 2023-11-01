# Install and load required packages
library(tm)
library(wordcloud)
library(RColorBrewer)

# Read the CSV file
scientists <- read.csv("output.csv", header = TRUE)

# Calculate the frequency of each term (country)
word_freq <- table(scientists$Field)

# Check for missing or zero frequency values
if (any(is.na(word_freq)) || all(word_freq == 0)) {
  stop("Invalid frequency values. Please check your data.")
}

# Set up a color palette for the word cloud
colors <- brewer.pal(9, "Reds")[1:length(unique(scientists$Country))]

# Create a word cloud with custom settings
wordcloud(
  words = names(word_freq),
  freq = as.vector(word_freq),

)
