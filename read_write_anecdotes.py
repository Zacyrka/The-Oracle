def read_anecdotes(filename):
    """
        Read anecdotes from a text file.

        Args:
            filename (str): The path to the file containing anecdotes.

        Returns:
            List of str: A list of anecdotes read from the file.
        """
    with open(filename, 'r', encoding='utf-8') as file:
        anecdotes = file.read().split('---')
        return [anecdote.strip() for anecdote in anecdotes if anecdote.strip()]

def write_anecdote_to_file(file_path, new_anecdote):
    """
        Write a new anecdote to a text file.

        Args:
            file_path (str): The path to the file where the new anecdote should be added.
            new_anecdote (str): The text of the new anecdote to be added.

        Returns:
            None
        """
    with open(file_path, 'a') as file:
        file.write('\n' + new_anecdote + '\n---')
