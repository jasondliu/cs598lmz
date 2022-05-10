import _struct from './struct';
import _new from './new';
import _structural from './structural';
import _typed from './typed';

// The following are base mixins for the entire library
export {
  _abstract,
  _algebraic,
  _declare,
  _immutable,
  _new,
  _struct,
  _structural,
  _typed
};

// The following are the mixins for the IO module
import _io_callback from './io/callback';
import _io_array from './io/array';
import _io_string from './io/string';
import _io_number from './io/number';
import _io_object from './io/object';

export {
  _io_callback,
  _io_array,
  _io_string,
  _io_number,
  _io_object
};

// The following are the mixins for the Validation module
import _validation_array from './validation/array';
import _validation_object from
