import selection from '../selection';

const getActionType = (action) => {
  if (action.type === 'paste') {
    return 'paste';
  }

  if (action.type === 'insert_characters') {
    return 'insert';
  }

  if (action.type === 'backspace_character' || action.type === 'delete_character') {
    return 'remove';
  }

  if (action.type === 'change_inline_style' && action.data.style.startsWith('DELETION')) {
    return 'deletion';
  }

  return 'style';
};

const isNonLineAction = (action) => {
  return (
    action.type === 'insert_characters'
    || action.type === 'backspace_character'
    || action.type === 'delete_character'
  );
};

const isLineChangeAction = (action) => {
  return (
    action.type === 'split_block'
    || action.type === 'merge_block_data'
  );
};

