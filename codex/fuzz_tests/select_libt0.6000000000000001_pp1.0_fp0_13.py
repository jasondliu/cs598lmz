import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getRepoURL} from '../github-helpers';
import {isEditable} from '../dom-utils';

function init(): void {
	// Ignore drafts
	if (select.exists('.btn-group-drafts')) {
		return;
	}

	// Add "Edit" button to the editable file header
	const editButton = `
		<button type="button" class="btn btn-sm BtnGroup-item" aria-label="Edit file">
			<svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l
