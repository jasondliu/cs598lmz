import select from 'select-dom';

export default new Tab('#pull-request-commits', 'Commits', () => {
	const navOnly = select.exists('#pull-request-commits > .branch-action-body');
	if (navOnly) {
		select('#pullrequest-content ~ .branch-action-body').classList.add('rgh-pr-commits-nav');
	}
});
