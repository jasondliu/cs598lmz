import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import * as api from '../github-helpers/api';

const getRepo: () => string = () => select('.repository-meta-content')!.textContent!.trim();

function init(): void {
	const repo = getRepo();

	const button = (
		<button
			type="button"
			class="btn btn-sm btn-danger"
			style={{marginLeft: '5px'}}
			title="Delete this repository"
			onclick={() => {
				if (confirm(`Are you sure you want to delete ${repo}?`)) {
					api.v3(`repos/${repo}`, {}, {method: 'DELETE'})
						.then(() => {
							location.href = `/${repo.split('/')[0
