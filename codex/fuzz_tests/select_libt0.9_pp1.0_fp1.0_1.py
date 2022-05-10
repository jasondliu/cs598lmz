import select from 'select-dom';
import * as search from './libs/search';
import onNewComments from './libs/on-new-comments';

export default function () {
	// Adds SHA to commit links
	addCommitSha();
	addCommitShaInMergeButton();
	// Adds link to branch
	addBranchLink();
	// Remix Dedup
	window.remix.dedupFileHeader();

	// Add a link to your fork's near the Repo's title
	window.remix.addYourForkToProjectHeader();

	// Append the .branch before each file path
	window.remix.prependCurrentBranchToFilePaths();

	// Append the .sha to each file path
	window.remix.prependCurrentCommitToFilePaths();

	// Binary tree
	onNewComments(() => {
		window.remix.addBinaryTreeToReviewComments();
	});

	// Linkify new review comments
	onNewComments(() => {
		window.remix.linkifyNewReview
