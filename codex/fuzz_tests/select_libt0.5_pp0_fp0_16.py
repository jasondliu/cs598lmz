import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import {wrap} from '../helpers/dom-utils';
import features from '.';

function init(): void {
	if (select.exists('.js-project-column-cards-container')) {
		// TODO: Make this work for the new project pages
		return;
	}

	// Add the button
	const button = <button className="btn btn-sm tooltipped tooltipped-n" type="button" aria-label="Move this column to the right">&rsaquo;</button>;
	for (const header of select.all('.project-column-header')) {
		header.append(button.cloneNode(true));
	}

	// Move the column
	for (const button of select.all<HTMLButtonElement>('.project-column-header > button')) {
		button.addEventListener('click', event => {
			const column = button.closest('.project-column');
		
