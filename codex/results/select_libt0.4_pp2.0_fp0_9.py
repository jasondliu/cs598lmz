import select from 'select-dom';
import {getRepoURL} from '../libs/utils';
import {getUsername} from '../libs/utils';

export default function () {
	const username = getUsername();
	const repoURL = getRepoURL();
	const repoName = repoURL.replace(`https://github.com/${username}/`, '');

	const branchSelect = select('.branch-select-menu');
	const branchName = branchSelect.querySelector('.js-select-button').textContent.trim();

	const repoBranchName = `${repoName}#${branchName}`;

	const clipboardButton = <button className="btn btn-sm" type="button" title="Copy to clipboard">{repoBranchName}</button>;
	clipboardButton.addEventListener('click', () => {
		navigator.clipboard.writeText(repoBranchName);
	});

	branchSelect.parentNode.insertBefore(clipboardButton, branchSelect);
}
