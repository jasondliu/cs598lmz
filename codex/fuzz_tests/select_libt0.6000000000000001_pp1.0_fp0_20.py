import select from 'select-dom';
import domLoaded from 'dom-loaded';
import {isRepoRoot} from '../libs/page-detect';
import features from '../libs/features';

async function init(): Promise<void> {
	await domLoaded;

	const header = select('.repository-content > header');
	if (!header) {
		return;
	}

	header.after(
		<div className="Box repository-homepage-sidebar">
			<div className="Box-header">
				<h2 className="Box-title">Homepage</h2>
			</div>
			<div className="Box-body">
				<p>
					<a href="/settings/pages" className="btn btn-sm">
						Edit site
					</a>
				</p>
			</div>
		</div>
	);
}

features.add
