import select from '../../components/select/select';

export const getSelectType = () => {
  const elem = document.querySelector('.select_type');

  for (const el of elem.options) {
    if (el.selected) {
      return el.value;
    }
  }
};

export const saveLocal = (item) => {
  let saved = localStorage.getItem('saved');
  let items = [];

  if (saved) {
    items = JSON.parse(saved) || [];
  }

  items.push(item);
  localStorage.setItem('saved', JSON.stringify(items));

  // makePage();
  select.init();
};
