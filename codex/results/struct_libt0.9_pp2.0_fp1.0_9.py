import _struct from './struct.js';
import _table from './table.js';
import _text from './text.js';
import _timer from './timer.js';
import _tuple from './tuple.js';
import _union from './union.js';

// NOTE:  the buffer gets replaced with something else by webpack,  so we don't
//        import it here...
import _buffer from './buffer.js';
import _endianness from './endianness.js';
import _packedArray from './packedArray.js';
import _packedStruct from './packedStruct.js';
import _packedTable from './packedTable.js';
import _packedTrace from './packedTrace.js';
import _trace from './trace.js';

const introspect = {

    /**
     * @class
     * @summary Intro inspection of DDL-defined types.
     * @description
     * <pre style="font-family:monospace;font-size:0.9em;color:black">
     *  ===================================================================
     * |
