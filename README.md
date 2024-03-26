<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Flashy - French Vocabulary Learning Application</h1>
<h2>Project Overview:</h2>
    <p>The Flashy project is a GUI application built using Python's Tkinter library. It serves as a flashcard system to help users learn French vocabulary. The application displays French words on the front of the flashcard, and upon user interaction, reveals the English translation on the back of the card. Users can mark their familiarity with words and proceed to the next card accordingly.</p>

  <h2>Features:</h2>
    <ol>
        <li><strong>Flashcard System:</strong> Displays French words and their English translations.</li>
        <li><strong>Interactive Interface:</strong> Users can flip the flashcards to reveal the translations and mark their familiarity with the words.</li>
        <li><strong>Dynamic Content:</strong> Words to be learned are loaded from CSV files, allowing for easy customization and expansion of the vocabulary.</li>
        <li><strong>Data Persistence:</strong> The application keeps track of learned words and updates the CSV file accordingly.</li>
    </ol>

   <h2>Installation Steps:</h2>
    <ol>
        <li><strong>Clone Repository:</strong> Clone the Flashy repository to your local machine.</li>
        <li><strong>Navigate to Project Directory:</strong> Open a terminal or command prompt and navigate to the project directory.</li>
        <li><strong>Install Dependencies:</strong> Ensure you have Python installed. Additionally, install the required packages by running:</li>
        <pre><code>pip install pandas</code></pre>
        <li><strong>Download Images:</strong> Download the images used in the application (`card_front.png`, `card_back.png`, `wrong.png`, `right.png`) and place them in the project directory.</li>
        <li><strong>Update Data Files:</strong> Ensure you have the CSV files `french_words.csv` and `words_to_learn.csv` in the project directory. You can use the provided files or create your own with French words and their English translations.</li>
        <li><strong>Run the Application:</strong> Execute the `flashy.py` script using Python. Navigate to the project directory in the terminal and run:</li>
        <pre><code>python flashy.py</code></pre>
    </ol>

   <h2>Usage:</h2>
    <p>Learn French by interacting with the flashcards displayed on the screen. Click on the buttons to indicate your familiarity with the words and proceed to the next card.</p>
</body>
</html>
