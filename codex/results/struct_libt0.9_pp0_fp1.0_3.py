import _struct from './_struct'
import _isFunction from './_isFunction'

export default function _filter(fn, obj) {

  if(_isFunction(fn) === false){
    throw new Error('[filter] First argument must be a function')
  }

  if(_struct(obj) === 'Object') {
    return Object.entries(obj)
      .filter(([k, v]) => fn(v, k, obj) === true)
      .reduce((acc, [k, v]) => _set(k, v, acc), {})
  }

  return obj.filter(fn)
}
