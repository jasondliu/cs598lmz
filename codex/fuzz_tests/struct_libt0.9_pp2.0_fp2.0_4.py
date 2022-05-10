import _struct from "./lib/struct";
import _time from "./lib/time";
import _type from "./lib/type";

export class lib {
  static get core() {
    return _core;
  }

  static get dom() {
    return _dom;
  }
  
  static get func() {
    return _func;
  }

  static get lang() {
    return _lang;
  }
  
  static get json() {
    return _json;
  }

  static get operator() {
    return _operator;
  }

  static get regExp() {
    return _regExp;
  }
  
  static get string() {
    return _string;
  }
  
  static get struct() {
    return _struct;
  }

  static get time() {
    return _time;
  }
  
  static get type() {
    return _type;
  }
}

export default lib;
