import select from 'select-dom';
import delegate from 'delegate';

import features from '.';
import * as api from '../github-helpers/api';

function init(): void {
	for (const commitStatus of select.all<HTMLDetailsElement>('.commit-build-statuses details-menu')) {
		const originalTitle = commitStatus.title;
		commitStatus.title = '';

		const originalSummary = select<HTMLSummaryElement>('summary', commitStatus);
		const lastUpdateText = originalSummary.textContent;
		let lastUpdateEl = originalSummary.querySelector<HTMLSpanElement>('span')!;

		delegate(commitStatus, 'summary', 'click', async () => {
			lastUpdateEl.classList.add('rgh-spinning-commit-status');

			const {target_url} = await api.v3(`repos/${getRepoURL().split('/')[1]}/commits/${targetContext(commitStatus).dataset.pjax!.replace('#', '')}/
