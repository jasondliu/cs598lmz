import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getCleanPathname} from '../github-helpers';

function init(): false | void {
	const pathname = getCleanPathname();

	if (select.exists('#js-repo-pjax-container')) {
		addFileLink();
	}

	if (pathname.includes('/tree/')) {
		addFileLink();
	}

	if (pathname.includes('/blob/')) {
		addFileLink();
	}

	function addFileLink(): void {
		const repoPath = select<HTMLAnchorElement>('.repo-root .js-repo-root a')!;
		const treePath = select<HTMLAnchorElement>('.repository-content .current-path .js-current-repository-branch a')!;

		const filePath = pathname.includes('/tree/')
			? select<HTMLAnch
