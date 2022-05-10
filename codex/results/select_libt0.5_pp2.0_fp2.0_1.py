import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';

function init(): void {
	const button = select('#partial-discussion-sidebar button[aria-label="Subscribe to this conversation"]');
	if (!button) {
		return;
	}

	const isSubscribed = button.classList.contains('selected');
	const buttonText = isSubscribed ? 'Unsubscribe' : 'Subscribe';

	button.textContent = buttonText;
	button.classList.toggle('btn-primary', !isSubscribed);
	button.classList.toggle('btn-danger', isSubscribed);
}

void features.add(__filebasename, {
	include: [
		pageDetect.isIssue,
		pageDetect.isPRConversation
	],
	init
});
