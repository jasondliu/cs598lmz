import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

function init(): void {
	const username = getUsername();
	for (const link of select.all<HTMLAnchorElement>('[href^="/search?q=author%3A"]')) {
		const author = link.pathname.match(/author%3A([^&]+)/)![1];
		if (author === username) {
			link.textContent = 'You';
		}
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isSearchResults
	],
	init
});
