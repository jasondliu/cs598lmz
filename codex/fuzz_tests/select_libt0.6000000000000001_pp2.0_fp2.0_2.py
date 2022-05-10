import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';

function init(): void {
	const [repo, owner] = select<HTMLAnchorElement>('.owner-reponame')!
		.textContent!
		.split('/');
	const configUrl = `https://github.com/${owner}/${repo}/settings/branches`;

	for (const link of select.all<HTMLAnchorElement>('.js-branch-delete')) {
		link.parentElement!.append(
			<a href={configUrl} className="muted-link">{link.firstChild!.textContent}</a>
		);
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isRepoRoot
	],
	init
});
