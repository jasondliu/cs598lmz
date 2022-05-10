import select from 'select-dom';
import * as pageDetect from 'github-url-detection';

import {wrap} from '../helpers/dom-utils';

function init(): void {
	const prFooter = select('.pull-request-index');
	if (prFooter) {
		wrap(prFooter, <hr className="rgh-clear-fix" />);
	}
}

void features.add(__filebasename, {
	include: [
		pageDetect.isPRConversation
	],
	init
});
