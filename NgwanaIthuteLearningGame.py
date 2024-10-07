import random
import time

# Welcome message
name = input("Enter your name: ")
print(f"Dumela {name}! :) Welcome to a Setswana learning game called Ngwana Ithute!")
print("-----------------------------------------------------------------------")

# Initialize level and round_num outside the loop
level = ""
round_num = 0


def load_phrases(file_path):
    """
    Load phrases from a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        list: List of phrases loaded from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return []


def is_meaningful_combination(noun, verb):
    """
    Check if a combination of noun and verb is meaningful based on Setswana grammar rules.

    Args:
        noun (str): Noun phrase.
        verb (str): Verb phrase.

    Returns:
        bool: True if the combination is meaningful, False otherwise.
    """
    # Setswana grammar rules example:
    # Check if the noun phrase ends with "mo" or "bo" and verb starts with "ke" or "o"
    noun_markers = ["mo", "bo", "o"]
    verb_prefixes = ["ke", "o", "o"]

    # Randomly select a marker from the lists
    random_noun_marker = random.choice(noun_markers)
    random_verb_prefix = random.choice(verb_prefixes)

    if noun.endswith(random_noun_marker) and verb.startswith(random_verb_prefix):
        return True
    return False


def generate_sentence(noun_phrases, verb_phrases):
    """
    Generate a hidden sentence by selecting a random meaningful combination of noun and verb.

    Args:
        noun_phrases (list): List of noun phrases.
        verb_phrases (list): List of verb phrases.

    Returns:
        str: Hidden sentence with underscores for the missing word.
    """
    # Create combinations
    sentence_combinations = [(noun, verb) for noun in noun_phrases for verb in verb_phrases]

    # Filter meaningful combinations based on Setswana grammar rules
    meaningful_combinations = [(noun, verb) for noun, verb in sentence_combinations
                               if is_meaningful_combination(noun, verb)]

    # Select a random meaningful combination
    if meaningful_combinations:
        selected_combination = random.choice(meaningful_combinations)

        # print(selected_combination) to see the template before guessing, this is for testing purposes'.

        return selected_combination
    else:
        return "No meaningful combinations found."


def hangman(template, max_attempts, time_limit):
    """
    Play the hangman game using the given template.

    Args:
        template (str): The sentence template.
        max_attempts (int): Maximum number of attempts allowed.
        time_limit (int): Time limit for the level in seconds.

    Returns:
        int: Points scored in the game.
    """
    start_time = time.time()  # Record the start time

    # Split the template sentence into a list of words
    template_words = ' '.join(template).split()

    # Generate a random index within the range of the number of words in the template
    hidden_word_index = random.randint(0, len(template_words) - 1)

    # Retrieve the word at the randomly selected index to be the hidden word
    hidden_word = template_words[hidden_word_index]

    # Hide the selected word with underscores
    hidden_sentence = ['_' if word == hidden_word else word for word in template_words]

    attempts = max_attempts  # Maximum number of attempts
    points = 5  # Fixed points for each round

    print(f"\nYou have {attempts} guesses and {time_limit} seconds. Good luck!")

    while attempts > 0:
        elapsed_time = round(time.time() - start_time)
        remaining_time = max(0, time_limit - elapsed_time)
        print(f"\nTime remaining: {remaining_time} seconds")
        print("\nGuess the missing word:")
        print(' '.join(hidden_sentence))
        guess = input("Enter your guess: ").strip()

        if guess.lower() == hidden_word.lower():
            print(f"Congratulations, {name}! You guessed the word.")
            points += attempts  # Award points based on remaining attempts
            break
        else:
            print(f"Incorrect guess :(  You have {attempts - 1} {'guesses' if attempts - 1 > 1 else 'guess'} left. "
                  f"Try again. You got this!")
            attempts -= 1
            points -= 1  # Deduct 1 point for every incorrect guess

            if attempts > 0:
                # Provide a hint using a different generated sentence
                hint_sentence = generate_sentence(noun_phrases, verb_phrases)
                print(f"Hint: {hint_sentence}")

            # Check if time limit is reached
            if elapsed_time >= time_limit:
                print("\nTime's up! You ran out of time.")
                points = 0
                break

    if attempts == 0:
        print(f"\nSorry, you ran out of attempts. The correct word was: {hidden_word.lower()}")
        points = 0

    return max(points, 0)  # Ensure points are non-negative


def generate_sentence_intermediate(noun_phrases, verb_phrases):
    """
    Generate a hidden sentence for the intermediate level.

    Args:
        noun_phrases (list): List of noun phrases.
        verb_phrases (list): List of verb phrases.

    Returns:
        list: List of words in the sentence template.
    """
    # Create combinations
    sentence_combinations = [(noun, verb) for noun in noun_phrases for verb in verb_phrases]

    # Filter meaningful combinations based on Setswana grammar rules
    meaningful_combinations = [(noun, verb) for noun, verb in sentence_combinations
                               if is_meaningful_combination(noun, verb)]

    # Select a random meaningful combination
    if meaningful_combinations:
        selected_combination = random.choice(meaningful_combinations)

        # Extract noun and verb from the selected combination
        noun, verb = selected_combination

        # Return the noun and verb without creating a sentence with placeholders
        return [word for word in (noun + " " + verb).split()]
    else:
        return []


def hangman_intermediate(template_words, max_attempts, time_limit):
    """
    Play the hangman game for the intermediate level using the given template.

    Args:
        template_words (list): List of words in the sentence template.
        max_attempts (int): Maximum number of attempts allowed.
        time_limit (int): Time limit for the level in seconds.

    Returns:
        int: Points scored in the game.
    """
    start_time = time.time()  # Record the start time

    # Generate indices for three hidden words
    hidden_word_indices = random.sample(range(len(template_words)), 3)

    # Replace the selected indices with underscores
    hidden_sentence = ['_' if index in hidden_word_indices else word for index, word in enumerate(template_words)]

    attempts = max_attempts  # Maximum number of attempts
    points = 10  # Fixed points for each round

    print(f"\nYou have {attempts} guesses and {time_limit} seconds. Good luck!")

    while attempts > 0:
        elapsed_time = round(time.time() - start_time)
        remaining_time = max(0, time_limit - elapsed_time)
        print(f"\nTime remaining: {remaining_time} seconds")
        print("\nGuess the missing phrase:")
        print(' '.join(hidden_sentence))
        guess = input("Enter your guess: ").strip()

        # Convert the guess to lowercase for case-insensitive comparison
        guess_lower = guess.lower()

        # Convert the correct hidden words to lowercase for comparison
        correct_words_lower = [template_words[index].lower() for index in hidden_word_indices]

        if guess_lower == ' '.join(correct_words_lower) or all(
                word.lower() in guess_lower for word in correct_words_lower):
            print(f"Great Job, {name}! You guessed the phrase correctly ^o^.")
            points += attempts  # Award points based on remaining attempts
            break
        else:
            print(
                f"Incorrect guess :(  You have {attempts - 1} {'guesses' if attempts - 1 > 1 else 'guess'} left. Don't "
                f"give up. Try again!")
            attempts -= 1
            points -= 2  # Deduct 2 points for every incorrect guess

            # Update the display with correct guesses
            for i, word in enumerate(template_words):
                if i in hidden_word_indices and word.lower() in guess_lower:
                    hidden_sentence[i] = word

            # Check if time limit is reached
            if elapsed_time >= time_limit:
                print("\n Oh No, Time's up! You ran out of time.")
                points = 0
                break

    if attempts == 0:
        # Get the complete sentence with the unhidden words
        complete_sentence = ' '.join(
            word if index not in hidden_word_indices else template_words[index] for index, word in
            enumerate(template_words))
        print(f"\nSorry, you ran out of attempts :(  The correct phrase was: {complete_sentence}")
        points = 0

    return max(points, 0)  # Ensure points are non-negative


def shuffle_phrases_advanced(noun_phrases, verb_phrases, max_attempts, time_limit):
    """
    Play the hangman game for the advanced level using the shuffled sentence.

    Args:
        noun_phrases (list): List of noun phrases.
        verb_phrases (list): List of verb phrases.
        max_attempts (int): Maximum number of attempts allowed.
        time_limit (int): Time limit for the level in seconds.

    Returns:
        int: Points scored in the game.
    """
    start_time = time.time()  # Record the start time

    # Generate a meaningful sentence
    meaningful_sentence = generate_sentence(noun_phrases, verb_phrases)

    # Randomly shuffle the words in the sentence
    words = meaningful_sentence[0].split() + meaningful_sentence[1].split()
    random.shuffle(words)

    # Join the shuffled words to form the shuffled sentence
    shuffled_sentence = ' '.join(words)

    attempts = max_attempts  # Maximum number of attempts
    points = 5  # Fixed points for each round

    print(f"\nYou have {attempts} guesses and {time_limit} seconds. Good luck!")

    while attempts > 0:
        elapsed_time = round(time.time() - start_time)
        remaining_time = max(0, time_limit - elapsed_time)
        print(f"\nTime remaining: {remaining_time} seconds")
        print("\nRearrange the sentence:")
        print(shuffled_sentence)
        guess = input("Enter your sentence: ").strip()

        if guess.lower() == meaningful_sentence[0].lower() + " " + meaningful_sentence[1].lower():
            print(f"Great Job, {name}! You rearranged the sentence correctly.")
            points += attempts  # Award points based on remaining attempts
            break
        else:
            print(
                f"Incorrect sentence :(  You have {attempts - 1} {'guesses' if attempts - 1 > 1 else 'guess'} left. "
                f"Try again.")
            attempts -= 1
            points -= 1  # Deduct 1 point for every incorrect guess

            # Check if time limit is reached
            if elapsed_time >= time_limit:
                print("\nTime's up! You ran out of time :( ")
                points = 0
                break

    if attempts == 0:
        print(
            f"\nSorry, you ran out of attempts. The correct sentence was: {meaningful_sentence[0]} {meaningful_sentence[1]}")
        points = 0

    return max(points, 0)  # Ensure points are non-negative


def display_examples(level):
    """
    Display examples at the beginning of each level.

    Args:
        level (str): The chosen level.
    """
    if level == "beginner":
        print("\nExample (Beginner): If the sentence is 'Ke _ dijo tse di monate', your guess could be 'ja'.")
        print("The complete sentence will be 'Ke ja dijo tse di monate'; 'ja' is a Setswana verb which means eat.")
        print("Think about the structure of the sentence [noun phrase + verb phrase] and use that to guess the "
              "missing words.")
    elif level == "intermediate":
        print("\nExample (Intermediate): In this level, the sentence is longer, and three words are hidden.")
        print("Your task is to guess the entire phrase correctly. Each underscore represents a hidden word.")
    elif level == "advanced":
        print("\nExample (Advanced): In this level, the sentence is shuffled.")
        print("Your task is to rearrange the words to form a meaningful sentence.")
        print("Example: Shuffled sentence - 'rata borotho Mpho go ja'")
        print("You need to rearrange it to - 'Mpho o rata go ja borotho'.")

    # Load noun and verb phrases from text files


noun_phrases = load_phrases(r'C:\Users\bida22-068\Downloads\Python Assignment 2023\Setswana noun phrases1.txt')
verb_phrases = load_phrases(r'C:\Users\bida22-068\Downloads\Python Assignment 2023\Setswana Verb Phrases.txt')

# Initialize total score
total_score = 0

while True:
    # Ask the player to choose a level
    print("\nChoose a level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    level_choice = input("Enter the number corresponding to your chosen level: ")
    level_mapping = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}

    if level_choice in level_mapping:
        level = level_mapping[level_choice]
        print(f"\nYou've chosen the {level} level. Let's get started!")

        # Set the time limit for each level
        time_limits = {"beginner": 90, "intermediate": 100, "advanced": 120}
        time_limit = time_limits.get(level.lower(), 60)  # Default to 60 seconds if level not found

        # Display examples at the beginning of each level
        display_examples(level.lower())

        # Set the number of rounds based on the chosen level
        num_rounds_per_level = {"Beginner": 3, "Intermediate": 4, "Advanced": 5}.get(level, 3)

        for round_num in range(1, num_rounds_per_level + 1):
            print(f"\nRound {round_num}")

            if level == "Intermediate":
                generated_sentence = generate_sentence_intermediate(noun_phrases, verb_phrases)
                round_score = hangman_intermediate(generated_sentence, max_attempts=4, time_limit=time_limit)
            elif level == "Advanced":
                shuffled_sentence = generate_sentence(noun_phrases, verb_phrases)
                round_score = shuffle_phrases_advanced(noun_phrases, verb_phrases,
                                                       max_attempts=3,
                                                       time_limit=time_limit)
            else:
                generated_sentence = generate_sentence(noun_phrases, verb_phrases)
                round_score = hangman(generated_sentence, max_attempts=5, time_limit=time_limit)

            total_score += round_score  # Add the points scored in the current round to the total score

            # Display the score at the end of each round
            print(f"\nYou earned {round_score} points")

            if round_num < num_rounds_per_level and round_score > 0:
                next_round = input("Do you want to proceed to the next round? (yes/no): ").lower()
                if next_round != 'yes':
                    break

        # Ask if the player wants to proceed to the next level after completing all rounds of the current level
        if round_num == num_rounds_per_level:
            next_level_choice = input(f"Congratulations {name} :) ! You completed the level. Do you want to proceed to "
                                      f"the next level? (yes/no): ").lower()
            if next_level_choice != 'yes':
                # Exit the loop if the player doesn't want to proceed to the next level
                print(f"\nGame over. Your total score is: {total_score}")
                break
            else:
                # Update level
                if level == "Beginner":
                    level = "Intermediate"
                elif level == "Intermediate":
                    level = "Advanced"
                else:
                    print(f"Congratulations{name}! You completed all levels. O ithuthile Setswana :) ")
                    break

                # Adjust time limit and display examples for the new level
                time_limit = time_limits.get(level.lower(), 60)
                display_examples(level.lower())

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
