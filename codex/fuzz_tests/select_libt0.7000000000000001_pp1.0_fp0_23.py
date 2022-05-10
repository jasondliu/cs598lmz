import select from 'select-dom';
import * as api from '../libs/api';

export default async function () {
	if (!select.exists('.js-repo-filter, .js-code-list')) {
		return;
	}

	const container = select('.js-repo-filter');

	const files = [];

	container.querySelectorAll('.js-code-list .js-navigation-open:not(.rgh-show-all)').forEach(item => {
		files.push(item.textContent);
	});

	const hide = !(await api.storage.hideShowAllFiles());

	const button = container.appendChild(document.createElement('details'));
	button.innerHTML = `
		<summary>
			<span class="Counter">${files.length}</span>
			<span class="text-small text-gray-light">Files</span>
		</summary>
		<div class="rgh-show-all-files-list details-dialog-content
