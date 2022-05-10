import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';

const newComment = () => select('.js-new-comment-form-actions') ?? false;

function init(): void {
	for (const form of select.all('.js-discussion .js-inline-comments-container .js-new-comment-form')) {
		form.closest('.js-discussion')?.after(form);
	}

	for (const replyButton of select.all('.js-inline-comment-form-container .js-new-inline-comment-form-container ~ .js-inline-comment-form-container')) {
		replyButton.firstElementChild?.remove();
	}
}

function initOnNewComment(): void {
	// `.js-new-comment-form-actions` is the `.timeline-comment-wrapper`
	newComment()?.append(select('.js-inline-comment-form-container'));
}

void features.add(__file
