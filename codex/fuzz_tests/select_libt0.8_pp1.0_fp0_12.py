import selectedArticlesReducer from './selectedArticlesReducer';
import articlesReducer from './articlesReducer';
import clippingsReducer from './clippingsReducer';
import searchReducer from './searchReducer';
import categoriesReducer from './categoriesReducer';

import { combineReducers } from 'redux';

const rootReducer = combineReducers({
  category: categoriesReducer,
  search: searchReducer,
  clippings: clippingsReducer,
  articles: articlesReducer,
  scroll: selectedArticlesReducer
});

export default rootReducer;
