from lzma import LZMADecompressor
LZMADecompressor

from typing import List, Union, Optional, Tuple, NewType
StringList = List[str]
BytesList = List[bytes]
MaybeString = Optional[str]
MaybeStringList = List[MaybeString]
CommaStringList = List[str]
MaybeFunc = Optional[_T_co]
MaybeTuple = Optional[Tuple[MaybeString, MaybeFunc]]
MaybeTupleList = List[MaybeTuple]
MaybeTupleListList = List[MaybeTupleList]
MaybeTupleListDict = Dict[MaybeString, MaybeTupleList]
MaybeDict = Optional[Dict[str, MaybeString]]
MaybeList = Optional[List[str]]
MaybeStringDict = Optional[Dict[str, str]]
MaybeModule = Optional[ModuleType]
MaybeContextManager = Optional[ContextManager[MaybeModule]]
MaybePath = Optional[Path]
MaybeGzipFile = Optional[GzipFile]
MaybeLZMADecompressor = Optional[LZMADecompressor]
MaybeBytesIO = Optional[BytesIO]
MaybeBytes = Optional[bytes]
MaybeUnion
