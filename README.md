# Reddit Comments Extractor

This project extracts comments from a Reddit text dump file using Python and BeautifulSoup.

## Prerequisites

- Python 3.8
- BeautifulSoup 

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Run the Extractor Script:**

    ```bash
    python extract_comments.py <input_file_path>
    ```

    Replace `<input_file_path>` with the path to the Reddit text dump file.

3. **Output:**

    The extracted comments will be saved to a file named `extracted_comments.txt` in the same directory.

4. **Handling Missing Comments:**

    If comments are not found in the original dump file, the script will attempt to extract them using the "old" Reddit URL. The modified URL will be printed, and the script will make another attempt.

## Example

```bash
python extract_comments.py /path/to/your/reddit_dump.txt
 ```

## Issues:
If you encounter any issues or have suggestions for improvement, please open an issue.

## Contribution
-Fork the project.
-Create your feature branch (git checkout -b feature/your-feature).
-Commit your changes (git commit -m 'Add some feature').
-Push to the branch (git push origin feature/your-feature).
-Open a pull request.

## License
This project is licensed under the MIT License
