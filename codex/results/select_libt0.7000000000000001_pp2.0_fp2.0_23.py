import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';

function init(): void {
	// See https://github.com/sindresorhus/refined-github/issues/2574
	// `select.exists` checks for `.mr-2` because it's the first class on the last child of `.js-issue-row`.
	// It's not ideal, but it's a lot faster than `selectAll('.js-issue-row')`
	if (select.exists('.js-issue-row [aria-label*="Unsubscribe"]') || select.exists('.js-issue-row .mr-2')) {
		const button = select<HTMLButtonElement>('.js-issues-show-subscribed')!;
		button.textContent = 'Show issues you\'re not subscribed to';
		button.dataset.hotkey = 'alt+s';
	}
}

void features.add({
	id: __filebasename,
	description: 'Adds
