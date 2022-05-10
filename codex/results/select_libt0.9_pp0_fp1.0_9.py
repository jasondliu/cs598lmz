import select from 'select-dom';
import elementReady from 'element-ready';

export async function logInForm() {
	await elementReady('.auth-form-body');
	const form = select('form');
	const passwordInput = select('[name="password"]', form);
	passwordInput.focus();
}

export function twoFactorForm() {
	const form = select('form');
	const keyInput = select('[name="key"]', form);
	keyInput.focus();
}

export async function handleErrors() {
	await elementReady('.form-group.is-error');
	if (location.pathname === '/login') {
		await logInForm();
	} else {
		twoFactorForm();
	}
}
