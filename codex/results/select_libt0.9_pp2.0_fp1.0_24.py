import selectedReducer from '../selectors/employees';

export default combineReducers({
    sidebar: sidebarReducer,
    employee: employeesReducer,
    selected: selectedReducer
})
