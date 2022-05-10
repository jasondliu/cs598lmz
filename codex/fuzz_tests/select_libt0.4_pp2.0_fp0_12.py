import selection from '../selection';

const {
  getSelectionStart,
  getSelectionEnd,
  setSelection,
  setCaretPosition,
} = selection;

const isAndroid = /Android/i.test(navigator.userAgent);

function getInput(el) {
  if (el.tagName === 'INPUT') {
    return el;
  }

  const { input } = el;
  return input;
}

function getCaretPosition(el) {
  return getSelectionStart(el);
}

function setCaretPosition(el, pos) {
  setCaretPosition(el, pos);
}

function getSelectionRange(el) {
  return {
    start: getSelectionStart(el),
    end: getSelectionEnd(el),
  };
}

function setSelectionRange(el, range) {
  setSelection(el, range.start, range.end);
}

function getValue(el) {
  return getInput(el).value;
}

function setValue
