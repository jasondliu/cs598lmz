import select from 'select-dom';
import features from '../libs/features';

function init(): void {
	for (const link of select.all<HTMLAnchorElement>('a.js-navigation-open')) {
		link.href = link.href.replace(/\/blob\//, '/');
	}
}

features.add({
	id: __featureName__,
	description: 'Replaces `/blob/` URLs with `/` URLs on the file list page.',
	screenshot: 'https://user-images.githubusercontent.com/1402241/56713019-d8f9e680-66f9-11e9-8f5c-27a1b0f6a0a2.png',
	include: [
		features.isRepoTree
	],
	load: features.onAjaxedPages,
	init
});
