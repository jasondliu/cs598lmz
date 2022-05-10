import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

function init(): void {
	const username = getUsername();
	for (const link of select.all<HTMLAnchorElement>(`
		.js-issue-row:not(.rgh-hide-owned) > .d-table-cell:first-child > a[href*="/issues/"]
	`)) {
		const issueAuthor = link.closest('.js-issue-row')!.querySelector<HTMLAnchorElement>('.opened-by a')!.textContent!.trim();
		if (issueAuthor === username) {
			link.closest('.js-issue-row')!.classList.add('rgh-hide-owned');
		}
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isDashboard
	],
	init
});
