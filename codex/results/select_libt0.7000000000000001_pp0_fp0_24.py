import select from 'select-dom';

/* eslint-disable-next-line import/prefer-default-export */
export function init(): void {
  const searchForm = select<HTMLFormElement>('#top_search_form');
  if (!searchForm) {
    return;
  }

  const searchInput = select<HTMLInputElement>('#top_search_form_input');
  if (!searchInput) {
    return;
  }

  const searchLabel = document.createElement('label');
  searchLabel.setAttribute('for', 'top_search_form_input');
  searchLabel.textContent = 'Search';
  searchForm.appendChild(searchLabel);

  searchInput.setAttribute('placeholder', 'Search');
  searchInput.setAttribute('aria-label', 'Search');
}
