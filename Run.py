import sys
from src.module1 import process_raw_data
from src.module2 import extract_comments
from src.module3 import save_comments_to_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Read raw data from file
    with open(f'Data/raw/raw_data_file.txt', 'r') as file:
        raw_data = file.read()

    # Module 1: Process raw data
    processed_data = process_raw_data(raw_data)

    # Module 2: Extract comments
    comments = extract_comments(processed_data)

    # Module 3: Save comments to file
    save_comments_to_file(comments, 'Data/processed/comment_file.txt')

if __name__ == "__main__":
    main()
