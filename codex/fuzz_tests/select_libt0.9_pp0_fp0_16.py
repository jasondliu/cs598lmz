import selectUser from './selectUser';
import userProfile from './userProfile';
import userList from './userList';
import string from './string';
import login from './login';

const reducers = combineReducers({
  saveUser,
  selectUser,
  userProfile,
  userList,
  string,
  login,
}, {});
export default reducers;
