import select from 'select-dom';
import delegate from 'delegate-it';

import features from '.';
import onNewComments from '../github-events/on-new-comments';

function init(): void {
	onNewComments(update);
	update();
}

function update(): void {
	for (const button of select.all<HTMLButtonElement>('button[type="submit"]')) {
		if (button.textContent === 'Save') {
			button.textContent = 'Update';
		}
	}
}

void features.add(__filebasename, {
	shortcuts: {
		'r s': 'Update'
	},
	include: [
		features.isIssue
	],
	init
}, {
	include: [
		features.isPR
	],
	waitForDomLoaded: false,
	init: () => {
		delegate(document, 'button[type="submit"]', 'click', event => {
			const prHeader = select('.js-issue-sidebar');
