import os

def search_word_in_files(folder_path, search_word):
    """
    Search for a word in all .txt files in the specified folder.

    Args:
        folder_path (str): Path to the folder containing .txt files.
        search_word (str): Word to search for.

    Returns:
        List[str]: Names of files containing the search word.
    """
    matching_files = []
    search_word = search_word.lower()  # Make search case-insensitive

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read file content and check for the word
                content = file.read().lower()  # Convert content to lowercase
                if search_word not in content:
                    matching_files.append(filename)

    return matching_files


# Example usage
if __name__ == "__main__":
    # Input: Folder path and search word
    folder_path = input("Enter the folder path: ").strip()
    search_word = input("Enter the word to search for: ").strip()

    if not folder_path:
        folder_path = "corpus_norm"  # Default folder path

    # Perform search
    result = search_word_in_files(folder_path, search_word)

    # Output results
    if result:
        print(f"The word '{search_word}' was found in the following file(s):")
        for file in result:
            print(f"- {file}")
    else:
        print(f"The word '{search_word}' was not found in any file.")
