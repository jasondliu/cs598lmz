import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

function init(): void {
	// Add "Your" to the "Notifications" tab
	const notificationsTab = select('[href="/notifications"]');
	if (notificationsTab) {
		notificationsTab.textContent = `Your ${notificationsTab.textContent}`;
	}

	// Add "Your" to the "Issues" tab
	const issuesTab = select('[href="/issues"]');
	if (issuesTab) {
		issuesTab.textContent = `Your ${issuesTab.textContent}`;
	}

	// Add "Your" to the "Pull Requests" tab
	const pullRequestsTab = select('[href="/pulls"]');
	if (pullRequestsTab) {
		pullRequestsTab.textContent = `Your ${pullRequestsTab.textContent}`;
	}

	// Add "Your" to the "Projects"
