import io
class File(io.RawIOBase):
    """The schofield File IO class.
    """
    
    def __init__(self, file=None):
        """Create a new file IO object.
        Creates a new file IO object.
        """
        import schofield.core as core
        
        # Store core.
        self.core = core
        
        # Flag: Is file open.
        self.is_open = False
        
        # Flag: Is file readonly.
        self.is_readonly = False
        
        # Path to file.
        self.file_path = None
        
        # Size of file.
        self.file_size = None
        
        # Number of sectors.
        self.number_of_sectors = None
        
        # Sector size.
        self.sector_size = None
        
        # Header magic.
        self.header_magic = None
        
        # Sector magic.
        self.sector_magic = None
        
        # Sector index.
        self.sector_index = []
        
        # Cached sectors.
        self
