import csv

def process_csv(input_file, output_file, num_observations=500):
    # Define the column headings you want to extract
    columns_to_extract = ["authfull", "inst_name", "cntry", "rank (ns)", "sm-field"]

    with open(input_file, 'r', newline='', encoding='utf-8', errors='replace') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        # Create CSV reader and writer objects
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=columns_to_extract)

        # Write the header to the output file
        writer.writeheader()

        # Iterate through each row of the input file
        row_count = 0
        for row in reader:
            if row_count < num_observations:
                # Create a new dictionary with only the desired columns
                new_row = {col: row[col] for col in columns_to_extract}
                # Write the new row to the output file
                writer.writerow(new_row)
                row_count += 1
            else:
                break

def change_header(input_file, output_file, custom_headers):
    # Read the CSV file
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        data = list(reader)

    # Replace headers with custom headers
    data[0] = custom_headers

    # Write the updated data to a new CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)
if __name__ == "__main__":
    # Replace 'input.csv' and 'output.csv' with your actual input and output file names
    process_csv('trial.csv', 'output_50.csv', num_observations=1000)
    New_headers = ['Scientist', 'Institute', 'Country', 'Rank', 'Field']
    change_header('output.csv', 'output_50.csv', New_headers)