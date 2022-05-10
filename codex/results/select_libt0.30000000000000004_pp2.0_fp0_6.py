import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import * as api from '../github-helpers/api';
import {getUsername} from '../github-helpers';

const getRepo = (): string => select('.js-repo-filter-tab.selected')!.textContent!.trim();

function init(): void {
	const username = getUsername();
	const repo = getRepo();

	for (const link of select.all<HTMLAnchorElement>('[data-hovercard-type="repository"]')) {
		api.v4(`
			repository(owner: "${username}", name: "${repo}") {
				${link.dataset.hovercardType!}(owner: "${link.pathname.split('/')[1]}", name: "${link.pathname.split('/')[2]}") {
					id
				}
			}
	
