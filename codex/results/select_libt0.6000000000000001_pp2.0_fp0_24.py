import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import {wrap} from '../helpers/dom-utils';
import features from '.';

function init(): void {
	for (const commitSha of select.all<HTMLAnchorElement>('.commit-sha')) {
		const [, branchName] = /^\s*\(?(?:(?:[^@\s]+)\/)?([^@\s]+)\)?\s*$/.exec(commitSha.textContent!)!;
		if (branchName) {
			wrap(commitSha, `<a href="/branches/${branchName}" class="rgh-branch-link">`);
		}
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isPR
	],
	init
});
