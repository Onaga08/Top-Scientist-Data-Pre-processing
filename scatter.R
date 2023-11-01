# Load the ggplot2 library
library(ggplot2)

# Read the CSV file into a data frame
# Replace 'output.csv' with the actual file name
# If the file is on the desktop, you can use a relative path
data <- read.csv("output_50.csv", header = TRUE)

# Create a scatter plot
ggplot(data, aes(x = Rank, y = Field)) +
  geom_point() +
  labs(title = "Scatter Plot of Rank vs Subfield",
       x = "Rank",
       y = "Fields")
