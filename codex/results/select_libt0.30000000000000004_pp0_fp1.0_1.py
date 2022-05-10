import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

function init(): void {
	const username = getUsername();
	for (const link of select.all<HTMLAnchorElement>('.js-issue-row > .title > a')) {
		const isOwnIssue = link.textContent!.startsWith(`${username}: `);
		if (isOwnIssue) {
			link.classList.add('rgh-is-own-issue');
		}
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isDashboard
	],
	init
});
