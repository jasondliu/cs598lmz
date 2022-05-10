import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getRepoURL, getUsername} from '../github-helpers';

function init(): void {
	const repoURL = getRepoURL();
	if (!repoURL) {
		return;
	}

	const username = getUsername();
	const [, , repoName] = repoURL.split('/');

	const link = `https://github.com/${username}/${repoName}/settings/hooks/new`;
	select('.subnav-links')!.append(
		<a href={link} className="btn btn-sm subnav-item">
			<svg className="octicon octicon-gear" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fillRule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88
