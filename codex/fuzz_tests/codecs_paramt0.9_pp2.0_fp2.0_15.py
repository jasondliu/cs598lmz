import codecs
codecs.register_error('replace_not_g', replace_not_g)

def reduce_lengthening(token):
    """
    Replace repetitions of character sequences of length 3 or greater

    E.g.,
    2995    laaanggguuuun
    2994    fuuuuuuuuu

    Args:
        token (str): the token to reduce

    Returns:
        a reduced token

    Acknowledgement:
        @article{DBLP:journals/corr/abs-1711-09175,
          author    = {Hamed Fadaee and
                       David Grangier and
                       Michael Auli and
                       Donald Metzler},
          title     = {End-to-end Automatic Speech Recognition using Attention-based
                       Recurrent NN: Second Place Solution to the
                       Fourth CHiME Speech Separation and Recognition Challenge (CHiME-4)},
          journal   = {CoRR},
          volume    = {abs/1711.09175},
          year      = {2017},
          url       = {http://arxiv.org/abs/1711.
