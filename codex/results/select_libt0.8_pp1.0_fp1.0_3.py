import select from 'select';

export default {
  controller: function ($scope, $element, $timeout, $attrs, $parse) {
    let search = '';
    let hash = {};
    let hash_lookup = [];
    let order = [];
    let items = [];
    let buffer = null;
    let buffer_timeout = null;
    let container = $element[0].querySelector('.ui-select-choices');
    let id_map = {};
    let selection_map = {};
    let length = 0;
    let term = $parse($attrs.uiSelectChoices)($scope);
    let buffer_length = $parse($attrs.buffer)($scope) || 0;
    let reload = $parse($attrs.reload)($scope);
    let orderBy = $parse($attrs.orderBy);
    let filter = $parse($attrs.filter);
    let ctrl = this;

    this.activate = (item) => {
      $timeout(() => {
        ctrl.activeIndex = ctrl.getIndex(
