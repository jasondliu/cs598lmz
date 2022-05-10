import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_top_rating_files(rating_files, top_n):
    """ get top n rating files according to the average rating score
    
    Parameters
    ----------
    rating_files: list of str
        a list of file paths for each user's rating file
    top_n: int
        the number of top files to be returned
    
    Returns
    -------
    top_files: list of tuple
        a list of (file_path, average_score)
    """
    top_files = []
    for path in rating_files:
        f = codecs.open(path, 'r', 'utf-8', 'strict')
        lines = f.readlines()
        f.close()
        total = 0
        for line in lines:
            if line != '':
                total += int(line.strip().split('\t')[2])
        avg_score = total / len(lines)
        top_files.append((path, avg_score))
    top_files.sort(key=lambda t
