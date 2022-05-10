import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

# Path to the data directory into which the cleaned data is saved.
# These data files are code-generated from the original data files in
# https://github.com/google-research-datasets/gap-coreference
# See the README.md in that repo for more info.
DATA_DIR = "data/gap-development"

# Path to directory where BERT pretrained models are saved.
PRETRAINED_MODEL_DIR = "pretrained_models/uncased_L-12_H-768_A-12"

# Path to directory where the fine-tuned model and tokenizer are saved.
FINETUNED_MODEL_DIR = "outputs"

# Path to directory where the predictions are saved.
PREDICTION_DIR = "predictions"

# The maximum total input sequence length after WordPiece tokenization.
# Sequences longer than this will be truncated, and sequences shorter
# than this will be padded.
MAX_SEQ_LENGTH = 384

#
