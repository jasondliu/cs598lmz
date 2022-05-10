import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import * as api from '../github-helpers/api';
import {getRepoURL} from '../github-helpers';

function init(): void {
	const branch = select<HTMLAnchorElement>('.branch-select-menu .select-menu-item.selected');
	if (!branch) {
		return;
	}

	const branchName = branch.textContent!.trim();
	const repoURL = getRepoURL();
	if (!repoURL) {
		return;
	}

	const [, owner, repo] = repoURL.match(/([^/]+)\/([^/]+)/)!;
	api.v3(`repos/${owner}/${repo}/branches/${branchName}`).then(({default_branch}) => {
		if (default_branch === branchName) {
			return;
		}

		branch.append(
