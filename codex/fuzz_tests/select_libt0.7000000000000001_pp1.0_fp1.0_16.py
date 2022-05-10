import select from 'select-dom';

import features from '.';
import * as api from '../github-helpers/api';

async function init(): Promise<void | false> {
	const fileEl = select('.js-file') as HTMLElement | null;
	if (!fileEl) {
		return false;
	}

	const repo = getRepoURL();
	const {url, tree_sha} = await api.v4(`
		repository(${repo}) {
			url
			tree_sha: object(expression: "HEAD:${location.pathname}") {
				... on Blob {
					url
					sha: oid
				}
			}
		}
	`);

	const [, , branch] = select('.branch-select-menu .js-select-button')!.textContent!.match(/^([\w-]+)\s/)!;
	const filePath = location.pathname.substr(repo.
