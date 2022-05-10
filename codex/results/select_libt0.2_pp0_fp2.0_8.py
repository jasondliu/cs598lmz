import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getRepoURL} from '../github-helpers';

function init(): void {
	const repoURL = getRepoURL();
	if (!repoURL) {
		return;
	}

	const repoPath = repoURL.pathname.replace(/^\//, '');
	const repoLink = `[${repoPath}](${repoURL})`;

	for (const link of select.all('.commit-tease a')) {
		link.textContent = link.textContent.replace(repoPath, repoLink);
	}
}

void features.add({
	id: __filebasename,
	description: 'Adds links to the repository in commit messages.',
	screenshot: 'https://user-images.githubusercontent.com/1402241/56745301-0a8e5b00-6780-11e9-8e2d-9f9a9a9e8
