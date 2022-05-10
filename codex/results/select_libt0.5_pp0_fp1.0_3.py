import select from 'select-dom';
import delegate from 'delegate-it';
import * as pageDetect from 'github-url-detection';

import features from '.';
import * as api from '../github-helpers/api';
import {getUsername} from '../github-helpers';

function init(): void {
	delegate(document, '.js-issue-row', 'click', (event: delegate.Event<MouseEvent, HTMLAnchorElement>): void => {
		const issueElement = event.delegateTarget;
		const issueNumber = issueElement.getAttribute('data-issue-number')!;
		const issueRepo = select('.js-repo', issueElement)!.textContent!.trim();
		const issueAuthor = select('.opened-by a', issueElement)!.textContent!.trim();
		const issueAuthorIsCurrentUser = issueAuthor === getUsername();
		const issueAuthorIsOrg = issueAuthorIsCurrentUser || select.exists('.avatar.avatar-user', issueElement);
		const issueState = select
