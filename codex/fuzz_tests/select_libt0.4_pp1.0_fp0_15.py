import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

function init(): void {
	for (const link of select.all<HTMLAnchorElement>('[data-hovercard-type="user"]')) {
		const username = getUsername(link.href);
		link.href = `/${username}?tab=stars`;
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isRepo
	],
	init
});
