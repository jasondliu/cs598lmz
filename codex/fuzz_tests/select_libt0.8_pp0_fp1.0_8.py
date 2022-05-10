import select from 'select-dom';
import delegate from 'delegate-it';
import {observe} from 'selector-observer';
import * as pageDetect from 'github-url-detection';

import features from '.';
import dropdownMenu from '../github-helpers/dropdown-menu';
import {getNestedValue} from '../github-helpers';

const sidebarClassname = 'rgh-repo-nav';
const selectedClassname = 'rgh-is-selected';
const itemClassname = 'rgh-item';
const itemReadmeClassname = `${itemClassname}-readme`;
const itemWikiClassname = `${itemClassname}-wiki`;
const itemCodeClassname = `${itemClassname}-code`;
const itemActionClassname = `${itemClassname}-action`;

const addSidebarToTree = repoNav => {
	const readmeLink = select(`
		.${sidebarClassname} .${itemClassname}[href$="/blob/master/README.md"],
	
