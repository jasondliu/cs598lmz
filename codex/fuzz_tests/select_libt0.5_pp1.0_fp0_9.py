import select from 'select-dom';
import {getRepoURL, getRepoGQL} from '../libs/utils';
import * as pageDetect from '../libs/page-detect';

const features = {
	init() {
		const repo = getRepoGQL();
		if (repo) {
			this.addLink(repo);
		} else if (pageDetect.isPRConversation()) {
			this.addLink(getRepoURL());
		}
	},

	addLink(repo) {
		const url = `/${repo}/network/dependents`;
		const {href} = select('[href^="/${repo}/network"]')!;
		const link = <a href={`${href}/${url}`}>Dependents</a>;
		select('[href^="/${repo}/network"]')!.after(link);
	}
};

void features;
