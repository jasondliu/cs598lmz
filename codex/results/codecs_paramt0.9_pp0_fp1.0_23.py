import codecs
codecs.register_error('remove_control',remove_control_characters)
"""
Write a function that loads in a JSON file and creates a single .txt file of all the labeled data
that will be used to learn the language model. 
Output one file for each language:
    (1) training file with the actual text to go into the model, 
    (2) training file with just cloze questions (the sentences to guess), 
    (3) gold file with the correct text to fill in the blanks.
Factors in the following:
    - Content that is too hard or too easy is filtered out of both the training and gold file. This is
      determined by the difficulty values associated with each token in the JSON file.
    - All samples have both blanked and original text. If there is only one original text but multiple
      blanked text, make sure that duplicates are randomly assigned to the different cloze questions.
"""    
def make_lm_text(input_file,output_file_prefix):
    """
    Input: 
        - input_file = directory for the input .json file
        - output_file_prefix = prefix for
