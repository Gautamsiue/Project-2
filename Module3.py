# module3.py

def save_comments_to_file(comments, output_file):
    """
    This module saves comments to a specified file.
    
    Parameters:
    - comments (list): List of comments.
    - output_file (str): Path to the output file.
    """
    # Your file saving logic here
    with open(output_file, 'w') as file:
        for comment in comments:
            file.write(comment + '\n')
