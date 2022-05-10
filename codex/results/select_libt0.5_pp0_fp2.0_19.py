import select from 'select-dom';
import {getUsername} from '../libs/utils';
import features from '../libs/features';

function init(): void {
	select('.discussion-sidebar-item.sidebar-assignee')!.remove();
}

features.add({
	id: __featureName__,
	description: 'Removes the "Assignee" sidebar item on PRs',
	screenshot: 'https://user-images.githubusercontent.com/1402241/56442471-6e8b6200-62e2-11e9-8b8c-8e9a1b7c6b9e.png',
	include: [
		features.isPRConversation
	],
	load: features.onAjaxedPages,
	init
});
