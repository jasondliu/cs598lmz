import selectable.html from './selectable.html!text';
import selectableEditor from './selectableEditor.js';

export default class Selectable {
  constructor(options) {
    this.element = options.element;
    this.callbacks = {
      start: options.start || false,
      change: options.change || false,
      finish: options.finish || false
    };
    this.itemListClass = options.itemListClass || 'item-list';
    this.itemClass = options.itemClass || 'item';
    this.selectedItemClass = options.selectedItemClass || 'selected';
    this.selectionRangeClass = options.selectionRangeClass || 'select-range';
    this.multipleItemSelectClass = options.multipleItemSelectClass || 'multiple-select';
    this.editor = options.editor;
  }

  static create(options) {
    if (!options.element) throw 'An element is required to create your Selectable instance.';
    return new Selectable(options);
  }

  static editor() {
    return selectableEditor;
  }
