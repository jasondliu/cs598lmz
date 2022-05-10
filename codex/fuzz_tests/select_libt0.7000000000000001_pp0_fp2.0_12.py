import select from 'select-dom';
import domLoaded from 'dom-loaded';

const removeElement = element => element && element.remove();

function getDismissButton() {
	const button = select('.rgh-dismiss-button');
	if (button) {
		return button;
	}

	const newButton = <button class="rgh-dismiss-button">Dismiss</button>;
	select('div.Box-body').append(newButton);
	return newButton;
}

function addDismissButton() {
	getDismissButton().addEventListener('click', event => {
		removeElement(event.target);
		removeElement(select('.rgh-header'));
	});
}

function addHeader() {
	const header = <div class="rgh-header Box Box--condensed">
		<h1 class="Box-title">Repository Health</h1>
		<p class="Box-title">This is a preview of the <a href="https://github.com/sindres
