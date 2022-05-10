import select from 'select-dom';
import {getUsername, getRepoURL} from '../libs/utils';
import features from '../libs/features';

function init(): void {
	for (const btn of select.all<HTMLButtonElement>('[data-disable-with]')) {
		const action = btn.getAttribute('data-disable-with');
		if (action === 'Watching' || action === 'Watch') {
			btn.closest('.Box-row')!.prepend(
				<a
					href={`https://github.com/${getUsername()}?tab=stars&q=user%3A${getUsername()}+repo%3A${getRepoURL()}`}
					className="btn btn-sm ml-2"
					data-hotkey="w"
				>
					<svg aria-label="star" className="octicon octicon-star" viewBox="0 0 16 16
