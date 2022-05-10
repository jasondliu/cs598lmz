import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';

function init(): void {
	for (const button of select.all<HTMLButtonElement>('[data-js-remove-note]')) {
		button.addEventListener('click', () => {
			button.closest('.timeline-comment')!.remove();
		});
	}
}

void features.add({
	id: __filebasename,
	description: 'Allows you to delete comments on your own pull requests.',
	screenshot: 'https://user-images.githubusercontent.com/1402241/43575117-3bc4b4bc-961d-11e8-9c27-9e1be8e8b2fb.gif'
}, {
	include: [
		pageDetect.isPRConversation
	],
	init
});
