import select from 'select-dom';
import {isEmpty} from '../libs/utils';

import features from '.';

function init(): void {
	const pageNumber = select<HTMLInputElement>('[name="page"]')!;
	const pageCount = parseInt(select<HTMLSpanElement>('.js-pages-count')!.textContent!, 10);
	const nextPage = parseInt(pageNumber.value, 10) + 1;
	const currentUrl = new URL(window.location.href);
	const nextUrl = new URL(window.location.href);

	nextUrl.searchParams.set('page', String(nextPage));

	if (nextPage <= pageCount) {
		const link = `<div class="text-center">
			<a href="${nextUrl.href}" class="btn btn-outline BtnGroup-item">
				${__('Next')}
			</a>
		</div>`;
		// Get available actions
		const actions = select('.boxed-group-list');
