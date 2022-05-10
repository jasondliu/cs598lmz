import _struct from './struct';
import _nested from './nested';

const _global = {};

// Apply all modules
_global.apply = (configuration) => {
    _boolean(_global, configuration);
    _struct(_global, configuration);
    _nested(_global, configuration);
};

// Exports
export default _global;
