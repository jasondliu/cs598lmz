import io
class File(io.RawIOBase):
	"""File(name: str, mode: str = 'r', buffering: int = -1, encoding: Optional[str] = None, errors: Optional[str] = None, newline: Optional[str] = None, closefd: bool = True, opener: Callable[..., Any] = None)
	Open a file.

	The returned object will have type 'io.FileIO' if the file was
	opened in binary mode or 'io.TextIOWrapper' otherwise.

	name is the path to be opened.
	mode is an optional string that specifies the mode in which
	the file is opened. It defaults to 'r'.
	buffering is an optional integer used to set the buffering policy.
	Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
	line buffering (only usable in text mode), and an integer > 1 to indicate
	the size of a fixed-size chunk buffer. When no buffering argument is given,
	the default buffering policy works as follows:

	Binary files are buffered in fixed-size chunks; the size of the buffer is
	
