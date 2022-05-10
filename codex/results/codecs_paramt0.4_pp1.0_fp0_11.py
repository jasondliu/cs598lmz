import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Définition des fonctions
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def get_args():
    """
    Récupération des arguments de la ligne de commande.
    """
    parser = argparse.ArgumentParser(description='Convertit un fichier de texte au format UTF-8 en fichier texte au format ISO-8859-1.')
    parser.add_argument('input_file', type=str, help='fichier à convertir')
    parser.add_argument('output_file', type=str, help='fichier converti')

    return parser.parse_args()

#------------------------------------------------------------------------------
def convert_file(input_file, output_file):
    """
    Convertit un fichier de texte au format UTF-8 en fichier texte au format ISO-8859-1.

    :param input_file: fichier à convertir
    :type input_file: str
    :param output_file: fich
