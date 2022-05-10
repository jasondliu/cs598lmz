import select from 'select-dom';
import {createAddSection} from './helpers/dom-element';
import supportsCSSVariables from '../libs/supports-css-variables';

const colorNames = {
	cyan: '#0ff',
	green: '#0f0',
	lightPurple: '#bf80ff',
	mediumPurple: '#a020f0',
	orange: '#ffa500',
	red: '#f00',
	teal: '#008080',
	yellow: '#ff0'
};

let defaultDarkValues = {};
let defaultLightValues = {};
for (const [name, value] of Object.entries(colorNames)) {
	defaultDarkValues[name] = `var(--${name}-dark)`;
	defaultLightValues[name] = `var(--${name}-light)`;
}

class Themes {
	static init() {
		// Update theme on update event to check if it should be enabled
		Hexo.Extend.filter
