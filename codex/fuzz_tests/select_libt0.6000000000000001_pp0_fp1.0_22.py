import select from 'select-dom';
import delegate from 'delegate-it';

import features from '.';
import * as api from '../github-helpers/api';
import {getRepoURL, getUsername} from '../github-helpers';
import {getUsernameFromUrl} from '../github-helpers/utils';

const getUsernameFromAnchor = anchor => anchor.pathname.split('/')[1];

function init(): void {
	delegate(document, '.user-profile-nav .UnderlineNav-body a', 'click', ({delegateTarget}) => {
		const username = getUsernameFromAnchor(delegateTarget);
		const repoURL = getRepoURL();
		const repoUsername = repoURL && getUsernameFromUrl(repoURL);

		if (
			repoUsername === username &&
			['overview', 'repositories', 'projects', 'stars', 'packages'].includes(select('.user-profile-nav .navigation-focus').id)
		) {
