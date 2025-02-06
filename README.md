# Setswana-Language-Learning-Game

This repository contains a Python-based language learning game designed to help users learn and practice Setswana, a Bantu language spoken in Southern Africa. The game focuses on improving vocabulary and understanding through interactive exercises with verbs and noun phrases.

## Flowchart showing Game Logic

[View the Flowchart](https://github.com/Deirdre24/Setswana-Language-Learning-Game/blob/main/PYTHON%20SetswanaLearningGame%20Flowchart.pdf)


## Features

- Interactive Gameplay: Engaging exercises to test and improve Setswana language skills.
- Dynamic Content: The game reads from text files containing Setswana verb and noun phrases, making it easy to update and expand the vocabulary.
- Beginner-Friendly: Simple and intuitive design suitable for learners at any level.

## Repository Structure

.
├── game.py                 # Main Python script for the game
├── verbs.txt               # Text file containing Setswana verbs
├── noun_phrases.txt        # Text file containing Setswana noun phrases
├── README.md               # Project documentation (this file)

## Requirements

Python 3.7 or later

## Libraries

The game uses only standard Python libraries, so no additional installations are required.

## How to Run the Game

Clone this repository:

git clone  https://github.com/Deirdre24/Setswana-Language-Learning-Game.git

## Navigate to the project directory:

cd setswana-language-game

## Run the Python script:

python game.py

Follow the prompts to start learning Setswana!

## How It Works

Ngwana Ithute is a Setswana learning game crafted as an innovative and engaging tool for early childhood learners. The game transforms Setswana learning into an adventure for Kindergarten students by merging education with enjoyment.

## Objectives

Immerse students in Setswana, fostering language engagement, vocabulary acquisition, and sentence construction.

Teach sentence structure in a playful environment, encouraging exploration and creativity.

Spark curiosity and positive attitudes toward language learning through increasingly challenging levels.

## Game Mechanics

The game uses the following mechanics to reinforce Setswana learning concepts:

Sentence Construction: Players interact with placeholders for noun phrases and verb phrases provided in two text files (verbs.txt and noun_phrases.txt). These placeholders are combined to create grammatically correct sentences using the generate_sentence() function, which filters phrases based on Setswana grammar rules.

Hangman Mechanism: Sentence templates with hidden words (underscores) challenge players to guess missing words, improving vocabulary and sentence familiarity.

Rearranging Shuffled Sentences: In advanced levels, players rearrange shuffled sentences, leveraging their understanding of basic Setswana sentence structure.

## Interactive Features

Players are prompted to enter their name at the start, personalizing feedback and congratulatory messages.

Visual elements such as smileys :) 😊 and :( ☹, as well as ^0^, mimic graphics that appeal to children.

A timer and point system add excitement and track progress.

## Randomized Sentence Generation

The generate_sentence() function ensures that sentences make sense grammatically by combining phrases based on Setswana grammar rules. It uses noun and verb markers to validate sentence combinations and randomizes content for variety.

## Customizing the Game

Updating Vocabulary

You can expand the vocabulary by editing the verbs.txt and noun_phrases.txt files:

``: Add one verb per line.

``: Add one noun phrase per line.

Ensure that the text files follow the same format to avoid errors.

## Modifying Game Logic

To change or add game mechanics, edit the game.py file. The code is structured for easy modification and extension.

## Contributing

Contributions are welcome! If you have suggestions for new features, bug fixes, or improvements, feel free to open an issue or submit a pull request


Happy learning! Ke a leboga! (Thank you!)

