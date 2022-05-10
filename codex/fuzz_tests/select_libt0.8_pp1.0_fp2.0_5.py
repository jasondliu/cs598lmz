import select from 'select-dom';
import elementReady from 'element-ready';
import domLoaded from 'dom-loaded';

import onPrMergeButtonClicked from './observers/pr-merge-click-observer';
import onPrMergeDialogueOpened from './observers/pr-merge-dialogue-observer';
import onPrDialogOpened from './observers/pr-dialog-observer';
import onIssueDialogOpened from './observers/issue-dialog-observer';
import onPrDragStarted from './observers/pr-drag-observer';
import onPrCommentsLoaded from './observers/pr-comments-observer';
import onMergedPRsLoaded from './observers/merged-prs-observer';
import onReleaseFormOpened from './observers/release-form-observer';
import onIssueCommentsLoaded from './observers/issue-comments-observer';
import onCodeReviewLoaded from './observers/code-review-observer
