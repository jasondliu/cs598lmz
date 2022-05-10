import select from 'select-dom'
import { getRepoURL } from '../libs/utils'
import * as pageDetect from '../libs/page-detect'

export default () => {
	const repoURL = getRepoURL()
	if (!repoURL) {
		return
	}

	// Don't add the button if there is already a "New pull request" button
	if (select.exists('a.btn[href$="/compare/"]')) {
		return
	}

	const branch = pageDetect.getBranch()
	if (!branch) {
		return
	}

	const newBranchButton = select('.file-navigation [title="Create new branch"]')
	if (!newBranchButton) {
		return
	}

	const newPullRequestButton = (
		<a
			className="btn btn-sm"
			href={`${repoURL}/pull/new/${branch}`}
			title="Open a pull request for this branch"
	
