import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

function init(): void {
	const username = getUsername();
	if (!username) {
		return;
	}

	for (const link of select.all<HTMLAnchorElement>(`
		.js-issue-row:not(.rgh-hide-issue-row),
		.js-issue-row:not(.rgh-hide-issue-row) ~ .js-issue-row
	`)) {
		const issue = select('.js-navigation-open', link);
		if (issue) {
			link.classList.toggle('rgh-hide-issue-row', issue.textContent!.includes(username));
		}
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isDashboard
	],
	init
});
