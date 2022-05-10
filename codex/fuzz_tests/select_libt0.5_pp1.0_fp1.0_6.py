import select from 'select-dom';

import features from '.';
import * as api from '../github-helpers/api';

async function init(): Promise<void> {
	const repo = getRepoURL();
	if (!repo) {
		return;
	}

	const [owner, repoName] = repo.split('/');
	const {data: releases} = await api.v3(`/repos/${owner}/${repoName}/releases`);
	if (!releases.length) {
		return;
	}

	const latestRelease = releases[0];
	if (latestRelease.prerelease) {
		return;
	}

	const latestReleaseTag = latestRelease.tag_name;
	const currentBranch = select<HTMLAnchorElement>('[itemprop="breadcrumb"] [itemprop="title"] a')!.textContent!;

	if (currentBranch === latestReleaseTag) {
		return;
	}

	const compareLink = `/${owner}/${repoName}/comp
