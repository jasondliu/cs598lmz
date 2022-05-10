import select from 'select-dom';

import features from '.';
import {getRepoURL} from '../github-helpers';

function init(): void {
	for (const username of select.all('.user-mention')) {
		username.title = 'Click to open the user\'s profile';
		username.href = getRepoURL() + '@' + username.textContent;
	}
}

void features.add({
	id: __featureName__,
	description: 'Converts `@username` mentions to links.',
	screenshot: 'https://user-images.githubusercontent.com/1402241/32503637-1f7a1b30-c3d9-11e7-8f62-b79906d4e4b8.gif'
}, {
	include: [
		features.isIssueOrPRConversation
	],
	waitForDomReady: false,
	init
});
