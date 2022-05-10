import select from 'select-dom';
import domLoaded from 'dom-loaded';
import * as pageDetect from 'github-url-detection';

import features from '.';

function init(): void {
	const prTitle = select<HTMLHeadingElement>('.js-issue-title')!;
	const prMeta = select<HTMLDivElement>('.gh-header-meta')!;
	const prTitleLink = select<HTMLAnchorElement>('a.js-navigation-open', prTitle)!;
	const prTitleLinkText = prTitleLink.textContent!;
	const prTitleLinkHref = prTitleLink.href;
	const prTitleLinkHrefParts = prTitleLinkHref.split('/');
	const prUser = prTitleLinkHrefParts[3];
	const prRepo = prTitleLinkHrefParts[4];
	const prNumber = prTitleLinkHrefParts[6];

	// Add a link to the PR on GitHub
	const prTitleLinkOnGitHub = document.createElement('a');
	prTitleLinkOnGitHub.
