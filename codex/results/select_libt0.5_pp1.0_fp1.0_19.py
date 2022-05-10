import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';

function init(): void {
	const sidebar = select('.vcard-details');
	if (!sidebar) {
		return;
	}

	const sidebarLinks = sidebar.querySelectorAll('a');
	if (sidebarLinks.length < 2) {
		return;
	}

	for (const link of sidebarLinks) {
		if (link.href.startsWith('https://github.com/')) {
			link.href = link.href.replace('https://github.com/', 'https://gitlab.com/');
		}
	}
}

void features.add({
	id: __filebasename,
	description: 'Replaces all GitHub links with GitLab links in the profile sidebar of the user page.',
	screenshot: 'https://user-images.githubusercontent.com/1402241/53480338-f5d50000-3a9f-11e9-8
