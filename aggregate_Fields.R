library(dplyr)

# Replace 'your_input_file.csv' with the actual name of your CSV file
input_file <- "output.csv"

# Read data from CSV
scientists <- read.csv(input_file)

# Aggregate data to get the count of scientists per country
aggregated_data_fields <- scientists %>%
  group_by(Field) %>%
  summarise(NumScientists = n())


# Save aggregated data to a new CSV file
write.csv(aggregated_data_fields, "aggregated_scientists_Fields.csv", row.names = FALSE)
