import os
import re

def search_word_in_files(folder_path, search_word):
    """
    Search for a word in all .txt files in the specified folder and extract context.

    Args:
        folder_path (str): Path to the folder containing .txt files.
        search_word (str): Word to search for.

    Returns:
        List[Tuple[str, List[str]]]: List of tuples containing file names and matching contexts.
    """
    matching_files = []
    search_word_lower = search_word.lower()  # Make search case-insensitive
    word_pattern = re.compile(r'\b{}\b'.format(re.escape(search_word)), re.IGNORECASE)

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Tokenize properly to match raw text positions
                words = re.findall(r'\b\w+\b', content)  # Extracts words only
                lower_words = [word.lower() for word in words]  # Case-insensitive matching
                
                contexts = []
                for i, word in enumerate(lower_words):
                    if word == search_word_lower:
                        # Get 3 words before and after the match
                        context = words[max(0, i - 3): i + 4]
                        contexts.append(" ".join(context))

                if contexts:
                    matching_files.append((filename, contexts))

    return matching_files


# Example usage
if __name__ == "__main__":
    # Input: Folder path and search word
    folder_path = input("Enter the folder path: ").strip()
    search_word = input("Enter the word to search for: ").strip()

    if not folder_path:
        folder_path = "corpus_norm_lem"  # Default folder path

    # Perform search
    result = search_word_in_files(folder_path, search_word)

    # Output results
    if result:
        print(f"The word '{search_word}' was found in the following file(s):")
        for file, contexts in result:
            for context in contexts:
                print(f"- {file}: {context}")
    else:
        print(f"The word '{search_word}' was not found in any file.")