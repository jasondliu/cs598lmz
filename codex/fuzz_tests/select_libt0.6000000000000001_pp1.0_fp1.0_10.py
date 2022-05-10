import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';
import {Observe} from '../github-events/dom-event-handler';

function init(): void {
	const username = getUsername();
	if (!username) {
		return;
	}

	const currentUserSelector = `[data-hovercard-type="user"][data-hovercard-url="/users/${username}/hovercard"]`;
	const currentUser = select(currentUserSelector);
	if (!currentUser) {
		return;
	}

	currentUser.classList.add('rgh-highlight-current-user-mention');

	// Remove the current user from the mentions dropdown
	Observe('.js-mention-suggestions', () => {
		for (const mention of select.all(currentUserSelector)) {
			mention.remove();
		}
	});
}

void features.add
