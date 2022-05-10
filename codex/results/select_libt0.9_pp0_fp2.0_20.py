import selectorListeners from './selector-listeners';
import { dasherize } from '../../util';

export default function(key, value) {
  let listeners = selectorListeners[key];
  if (listeners) {
    Object.keys(listeners).forEach(selectorKey => {
      listeners[selectorKey].forEach(listener => {
        let selector = listener.selector;
        let property = listener.property;

        let calls = this.select(selector);
        calls.forEach(el => {
          if (!el) {
            return;
          }

          append(el, value, property);

          let [camelizedKey, dividers] = camelizeProperty(key);
          let selectedKey = camelizedKey;

          if (listener.hasOwnProperty('key')) {
            selectedKey = listener.key;
          } else if (listener.hasOwnProperty('dasherize')) {
            dividers = dividers || [];
            selectedKey = dasherize(key, dividers);
          }

          el.setData
