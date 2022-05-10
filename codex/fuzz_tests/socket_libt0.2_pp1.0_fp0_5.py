import socket
import sys
import time
import threading
import random
import os
import subprocess

# Global variables

# The port number to listen on
port = 0

# The socket used to listen for incoming connections
serverSocket = None

# The socket used to communicate with a client
clientSocket = None

# The maximum number of queued connections
backlog = 5

# A boolean flag set when the server should shut down
shutdown = False

# The name of the file containing the leaderboard
leaderboardFilename = "leaderboard.txt"

# The name of the file containing the questions
questionsFilename = "questions.txt"

# The name of the file containing the answers
answersFilename = "answers.txt"

# The name of the file containing the high scores
highScoresFilename = "highscores.txt"

# The name of the file containing the current scores
currentScoresFilename = "currentscores.txt"

# The name of the file containing the current questions
currentQuestionsFilename = "currentquestions.txt"

# The name of the file containing
