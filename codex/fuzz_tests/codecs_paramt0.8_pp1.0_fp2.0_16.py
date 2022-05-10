import codecs
codecs.register_error("strict", codecs.IGNORE_ERRORS)

from _utils import get_in, get_out, parse_args, encode, decode

def sentence_has_german_word(sentence, german_words):
    for token in sentence:
        if token["word"] in german_words:
            return True
    return False


def filter(in_f, out_f, german_words):
    in_json = json.loads(in_f.read())
    out_json = []
    for paragraph in in_json:
        german_sentences = [sentence for sentence in paragraph["sentences"] if sentence_has_german_word(sentence, german_words)]
        if len(german_sentences) > 0:
            new_paragraph = {
                "sentences": german_sentences,
            }
            if "speaker" in paragraph:
                new_paragraph["speaker"] = paragraph["speaker"]
            out_json.append(new_paragraph)
    out_f.write(encode(json.d
