import selectors from '../selectors/index';
import constants from '../constants/index';

export default class Store {
  constructor(initialState = {}, reducers = {}, middlewares = []) {
    this.state = initialState;
    this.reducers = reducers;
    this.middlewares = middlewares;
  }

  dispatch(action) {
    this.state = this.reducers[action.type](this.state, action);
    this.middlewares.forEach(middleware => middleware(this.state));
  }

  getState() {
    return this.state;
  }
}
