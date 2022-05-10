import select from 'select-dom';
import {getUsername} from '../libs/utils';

export default () => {
	const username = getUsername();
	if (username) {
		const userLink = select('.header-nav-current-user a');
		if (userLink) {
			userLink.href += `?tab=stars&q=user%3A${username}`;
		}
	}
};
