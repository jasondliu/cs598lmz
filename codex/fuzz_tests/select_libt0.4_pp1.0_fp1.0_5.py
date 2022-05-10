import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import * as api from '../github-helpers/api';
import {getUsername} from '../github-helpers';

function init(): void {
	const username = getUsername();
	for (const userLink of select.all<HTMLAnchorElement>(`
		.js-issue-sidebar-form .js-username,
		.js-issue-sidebar-form .js-user-profile-link
	`)) {
		if (userLink.textContent === username) {
			userLink.classList.add('rgh-current-user');
		}
	}
}

function getAssignees(): Promise<string[]> {
	return api.v4(`
		repository(owner: "${repo.owner}", name: "${repo.name}") {
			assignableUsers(first: 100) {
				nodes {
			
