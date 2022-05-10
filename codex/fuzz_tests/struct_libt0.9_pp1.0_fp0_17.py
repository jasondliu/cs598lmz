import _struct from './_struct'

/**
 * @name pick
 * @category Object
 * @since v0.24.0
 * @description
 * Picks properties from an object based on a set of keys, preserving the order.
 * The input object remains unmodified.
 *
 * @example
 * pick('a', { a: 1, b: 2 }) // => { a: 1, b: undefined }
 *
 * // It's also curried
 *
 * const p = pick('a', { a: 1, b: 2 })
 *
 * p({ a: 1, b: 2 }) // => { a: 1, b: undefined }
 * p({ a: 4 })       // => { a: 4 }
 * p({})             // => { a: undefined }
 */
export default _curry2((keys, obj) => {
  const result = (isString(keys) || isArray(keys))
    ? _struct(keys, [])
    : {}

  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      result[key] = obj[
