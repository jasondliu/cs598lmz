import select from 'select-dom';
import tagIcon from '../images/tag.svg';
import '../styles/tree.css';
import TimeHelper from '../modules/time-helper';

export default () => {
  const form = select('.js-release-form');
  if (!form) {
    return;
  }
  const tags = JSON.parse(select('[name="release[tag_name]"]')!.getAttribute('data-autocomplete-original-values') ?? '[]');
  const target = select('[name="release[target_commitish]"]')!;
  const title = select('[name="release[name]"]')!;
  const description = select('[name="release[body]"]')!;

  const container = <div className="container container-release-tree"></div>;
  form.prepend(container);

  const rawURL = new URL(`https://raw.githubusercontent.com/${GH_REPO}/`);
  const baseURL = new URL(`https://github.com/${GH_REPO}
