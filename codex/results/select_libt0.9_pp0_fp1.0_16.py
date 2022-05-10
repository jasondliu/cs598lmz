import selectView from '../selectViews';

export default function(state = [], action) {
	switch(action.type) {
		case SET_CURRENT_USER:
			const user = action.payload;
			let data = null;

			if (user.facebook) {
				data = selectView(user.name, user.email, user.facebook.id, user.facebook.accessToken, user.id)
			} else {
				data = selectView(user.name, user.email, null, user.id)
			}

			return data;
		default:
			return state;
	}
}
