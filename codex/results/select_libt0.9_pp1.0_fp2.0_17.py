import select from 'select-dom';
import features from '../libs/features';
import * as api from '../libs/api';

function makeLargeForces(container: Element): void {
	const map = select('.octolinker-map', container);
	if (!map) {
		return;
	}

	// Find exact width because `clientWidth` is floored; JS is precise
	const width = getComputedStyle(map).width.replace('px', '');
	// `naturalWidth` is what the image is *really*
	const height = map.naturalHeight * parseInt(width, 10) / map.naturalWidth;
	map.style.height = `${height}px`;

	// Can't use `:root` because of Shadow DOM
	map.closest('html')!.classList.add('rgh-large-forces');
}

async function init(): Promise<void> {
	// This renders the map at the moment (the DOM emits but doesn't render), but GH might change that at any time.
	document.addEventListener('ghmo
