import select from 'select-dom';
import delegate from 'delegate';

const list = select('.css-nav');

const getListItem = (title) => `
  <li class="css-nav__item">
    <a href="#${title}" class="css-nav__link css-nav__item--is-active">${title}</a>
  </li>
`;

const addListItems = () => {
  select.all('h2').forEach((title, index) => {
    var child = getListItem(`chapter_${index + 1}`);
    list.appendChild(child);
  });
};

const assignFirst = () => {
  select('.css-nav__link').classList.add('css-nav__item--is-active');
};

const setupActiveLink = () => {
  delegate('.css-nav__link', 'click', (event) => {
    select('.css-nav__link--is-active').classList.remove('css-nav__item--is-active');
    event.currentTarget.
