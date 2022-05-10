import select from 'select-dom';
+import {getUsername, getRepoURL} from '../libs/page-detect';
+import {getMergeButton} from '../libs/dom-utils';
+import {getRepoGQL} from '../libs/graphql-client';
+
+function isAutoMergeEligible(): boolean {
+	const hasBranchProtectionFromAdmins = select.all('.branch-infobar-text').some((el) =>
+		el.textContent?.includes('must be approved by')
+	);
+
+	const pullRequest = select('.gh-header-title');
+	const hasRequestedReview = select.all('.timeline-comment-header-text').some((el) =>
+		el.textContent?.trim()?.startsWith('Requested')
+	);
+
+	return !hasBranchProtectionFromAdmins && pullRequest && hasRequestedReview;
+}
+
+function isAutoMergeEnabled(): boolean {
+	return !!select
