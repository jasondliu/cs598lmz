import select from 'select-dom';
import * as icons from '../libs/icons';
import {getRepoURL} from '../libs/utils';
import {getRepoGQL, respondToAFriendGQL} from '../libs/graphql';

export default function () {
	const repo = getRepoURL();
	const username = select('.reponav-item + .reponav-item + .reponav-item')
		.querySelector('a')!
		.textContent!
		.trim();

	const octoCatElement = (
		<React.Fragment key="friend-link-reacat">
			{' '}
			<strong>{username}</strong> is a friend of{' '}
			<a
				href="https://github.com/sindresorhus"
				className="repo-snipit-owner css-truncate-target"
			>
				sindresorhus
		
