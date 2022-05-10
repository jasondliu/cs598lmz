import select from 'select-dom';
import {getUsername} from '../libs/utils';
import features from '../libs/features';

function init(): void {
	select('.js-repo-filter')!.before(
		<div className="mb-2">
			<label className="d-block f5 text-gray-dark">
				<input type="checkbox" className="mr-1" checked={!features.isDisabled('hide-forked-repos')} onChange={toggle}/>
				Hide forked repositories
			</label>
		</div>
	);
}

function toggle(event: Event): void {
	const forkedRepositories = select.all('.repo-list-item:not(.fork)');
	for (const repository of forkedRepositories) {
		repository.classList.toggle('rgh-hide-forked-repos', !(event.target as HTMLInputElement).checked);
	}
}

features.add({
	id
