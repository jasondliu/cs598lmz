import _struct_1 from './_struct';
import _invoke_1 from './_invoke';
import _xwrap_1 from './_xwrap';
import _isArray_1 from './_isArray';
import _slice_1 from './_slice';
var XWrap = /*#__PURE__*/_curry2_1(_xwrap_1.default);
var Bind = /*#__PURE__*/function () {
    function Bind(f, args) {
        this.f = f;
        this.args = args;
    }
    Bind.prototype.arity = function () {
        return this.args.length;
    };
    Bind.prototype.func = function () {
        return this.f;
    };
    Bind.prototype.args = function () {
        return this.args;
    };
    Bind.prototype.toString = function () {
        return 'Bind';
    };
    Bind.prototype.inspect = function () {
        return this.toString();
    };
    return Bind;
}();
var _arity_1 = _
