import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import features from '.';
import {getUsername} from '../github-helpers';

const userUrl = `/${getUsername()}`;
const userUrlPattern = new RegExp(`^${userUrl}(?:/|$)`);

function addReturnToProfileLink(): void {
	const url = select('.repohead-details-container h1 a, .reponav-item.selected a')!;
	const returnLink = <span className="rgh-return-to-profile octicon octicon-chevron-left" />;
	const link = (
		<a href={userUrl}>
			{returnLink}
			{url.textContent}
		</a>
	);

	link.classList.add(...url.classList);
	url.replaceWith(link);
}

function init(): void {
	if (userUrlPattern.test(location.pathname)) {
		addReturn
