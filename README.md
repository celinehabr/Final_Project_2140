# Final_Project_2140
This application is an interative quiz game about the environment and climate change. 

Dependencies:
- Python: The game is written in Python so the user is required to have Python, Visual Studios, or any other software that allows Python to run.
- Tkinter: This is the standard Python GUI library that comes pre-installed with Python.
- Messagebox: This is a library that is located within Tkinter and is needed to display the final score at the end of the game.
- JSON: The quiz game uses JSON for loading quiz questions. The JSON library is also a part of Python's standard library and doesn't require separate installation.

Limitations
- GUI Appearance: Because this game uses Tkinter, the appearance of the GUI might vary slightly across different operating systems, for example windows vs Mac.
- Input Questions Format: The game requires the quiz questions to be formatted and stored in a JSON file. The structure of this JSON file must match the expected format (with keys like 'text', 'choices', 'answer', 'category', and 'type'). An error will arise if the JSON file is formatted wrongly, causing the game to crash or behave unexpectedly.
- Input Validation: The game does not have extensive error handling for user inputs, however it is not necesary because the user is not typing any inputs, only clicking on the option. Entering unexpected data types or values in the quiz interface might lead to crashes or errors.

How to play:
- First ensure that all the files necessary are in the same diretcory. The files are final_project.py and quiz_questions.json.
- Once all the files are in the same directory, open the final_project file and run the code or type in the Python command line 'final_project.py'. 
- When launched, the game presents a start screen with the game's title and a button to begin the quiz.
- The user then selects the quiz difficulty that they want to play in (Easy Mode or Hard Mode).
- Once the category is chosen, the quiz starts and shows one question at a time with multiple choices or true or false.
- The user presses on the option they want as their answer and then presses the confirm button.
- Depending on whether the answer is correct or wrong, "Wrong" or "Right" will appear in the window, correspondingly.
- After the user has answered all the questions, the game will displays the user's final score and they will have to press the 'OK' button to close it. 
