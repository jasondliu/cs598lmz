import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape_error)

logger = logging.getLogger(__name__)

def extract_zips(zip_dir, dest_dir):
    """Extract all the zip files in the given directory to the destination directory."""
    logger.info('Extracting zips in %s to %s', zip_dir, dest_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    zip_paths = glob.glob(os.path.join(zip_dir, '*.zip'))
    for zip_path in zip_paths:
        logger.debug('Extracting %s', zip_path)
        zip_file = zipfile.ZipFile(zip_path)
        for filename in zip_file.namelist():
            # Check filename encoding
            if sys.version_info[0] > 2:
                try:
                    filename.encode('ascii')
                except UnicodeEncodeError:
                    filename = filename.dec
