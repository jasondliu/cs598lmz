import _struct from './struct'

function _toConsumableArray(arr) {
  if (Array.isArray(arr)) {
    for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) {
      arr2[i] = arr[i]
    }
    return arr2
  } else {
    return Array.from(arr)
  }
}

export default function unpack(_ref) {
  var strategy = _ref.strategy,
    _ref$decompress = _ref.decompress,
    decompress = _ref$decompress === undefined ? true : _ref$decompress,
    buffer = _ref.buffer
  var bytesProcessed = 0

  var _struct = struct(buffer),
    _struct2 = _slicedToArray(_struct, 2),
    header = _struct2[0],
    offset = _struct2[1]

  bytesProcessed += offset
  var data = _struct3(buffer.slice(offset))

  bytesProcessed += data.bytes

  var pack
