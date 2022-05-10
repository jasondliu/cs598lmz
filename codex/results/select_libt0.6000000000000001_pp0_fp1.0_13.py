import select from 'select-dom';
import * as icons from '../libs/icons';
import {groupSiblings} from '../libs/group-buttons';

const isPR = location.pathname.includes('/pull/');
const isPRFiles = location.pathname.includes('/pull-requests/');

export default function () {
	let button;
	if (isPRFiles) {
		button = select('.pr-toolbar .btn-group-merge');
	} else if (isPR) {
		button = select('.gh-header-actions .btn-group-merge');
	} else {
		return;
	}

	// If there is any button, there is a merge button too
	if (button) {
		button.before(
			<details className="details-reset details-overlay select-menu float-left">
				<summary className="btn btn-sm">
					{icons.merge()}
					{isPRFiles ? 'Merge'
