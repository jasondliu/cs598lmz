import select from 'select-dom';
import {getUsername} from '../libs/utils';
import * as pageDetect from '../libs/page-detect';

const getTitle = () => {
	const element = select('.js-issue-title');

	if (element) {
		return element.textContent;
	}

	return document.title;
};

const getBody = () => {
	const element = select('.js-comment-body');

	if (element) {
		return element.textContent;
	}

	return null;
};

const getLabels = () => {
	const labels = [];
	for (const label of select.all('.labels .label')) {
		labels.push(label.textContent.trim());
	}

	return labels;
};

const getExtraInfo = () => {
	const extraInfo = [];

	const assigneeElement = select('.js-assignee');
	if (assigneeElement) {
		extraInfo.push(`Assigned to:
