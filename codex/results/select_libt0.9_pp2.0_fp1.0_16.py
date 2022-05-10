import selectors from '../selectors';
import models from '../models';

import { createCollection, createApi } from '../../../services/utils';
import { wrapApiPromise } from '../../../utils/common';

import viewModule from '../viewModel';

// (selector) => Observable
function select(selector) {
  return this.map(selector).distinctUntilChanged();
}

function bindAction(store$, action, key) {
  let action$ = store$.map(action).take(1);
  if (!isObservable(action$)) action$ = Observable.just(action$.shareReplay(1));
  return this.merge(action$.map((data) => ({ [key]: data })))
}

// action => void
function dispatch(action) {
  return Rx.Observable.fromPromise(wrapApiPromise(action));
}

// { key: selector, ...} => Observable({ key: value, ...})
function bindSelectors(selectors) {
  let binder = this;

