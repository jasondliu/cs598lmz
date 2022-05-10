import select from 'select-dom';
import {getUsername, getRepo} from '../libs/utils';
import {isUserProfile, isRepo} from '../libs/page-detect';
import {observe} from '../libs/page-monitor';

export default function () {
	if (isUserProfile() || isRepo()) {
		observe('.js-profile-editable-area', {
			add(description) {
				description.append(`
					<div class="rgh-profile-readme">
						<h3>
							<a href="/${getUsername()}/${getRepo()}/blob/master/README.md">
								<svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1
