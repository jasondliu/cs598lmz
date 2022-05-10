import selectedCards from './selectedCards';
import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';

const reducer = combineReducers({
    cards,
    selectedCards,
    form: formReducer
});

export default reducer;
