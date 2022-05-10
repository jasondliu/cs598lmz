import selectedReducer from './selected_reducer';
import { combineReducers } from 'redux';
import ListReducer from './list_reducer';
const rootReducer = combineReducers({
  users: usersReducer,
  selected: listReducer
});

export default rootReducer;
