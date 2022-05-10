import _struct from './struct'
import _func from './func'
import _non_observable from './non-observable'

let _observable_cache = []

export default function _observable(value) {
    if (_observable_cache.indexOf(value) > -1) {
        return true
    }
    if (_struct(value)) {
        return false
    }
    if (_func(value)) {
        return false
    }
    if (_non_observable(value)) {
        return false
    }
    _observable_cache.push(value)
    return true
}
