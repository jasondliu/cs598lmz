import select from 'select-dom';
import {getUsername} from '../libs/utils';
import {getRepoURL} from '../libs/page-detect';

export default function () {
	const repoLink = select('.discussion-sidebar-item.discussion-sidebar-heading a');
	if (repoLink) {
		const username = getUsername();
		const repo = getRepoURL();
		const url = `https://github.com/${username}/${repo}/graphs/contributors`;
		repoLink.href = url;
	}
}
