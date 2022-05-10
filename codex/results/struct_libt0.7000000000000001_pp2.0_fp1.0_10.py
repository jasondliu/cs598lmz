import _struct from '../../util/struct'
import _json from '../../util/json'

const isArray = _struct.isArray

const toArray = val => (isArray(val) ? val : [val])

const join = (arr, delimiter = ',') => toArray(arr).join(delimiter)

const extract = (obj, keys = []) => {
  keys = toArray(keys)
  return keys.reduce((res, key) => {
    res[key] = obj[key]
    return res
  }, {})
}

const filter = (obj, keys = []) => {
  keys = toArray(keys)
  return Object.keys(obj).reduce((res, key) => {
    if (keys.includes(key)) {
      res[key] = obj[key]
    }
    return res
  }, {})
}

const exclude = (obj, keys = []) => {
  keys = toArray(keys)
  return Object.keys(obj).reduce((res, key) => {

