import selected_courses from './selected_courses';
import { combineReducers } from 'redux';

const rootReducer = combineReducers({
  courses, selected_courses
});

export default rootReducer;
