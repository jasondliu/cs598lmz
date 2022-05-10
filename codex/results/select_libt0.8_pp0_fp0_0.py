import selectors from './selectors';
import actions from './actions';

export default (createReducer = (initialState = {}) => {
  return handleActions(
    {
      ...handleAction('page', selectors.page, (state, payload) => ({ ...state, page: payload })),
      ...handleAction('pageSize', selectors.page, (state, payload) => ({ ...state, pageSize: payload })),
      ...handleAction(
        'setMovies',
        selectors.setMovies,
        (state, payload) => ({
          ...state,
          ...payload,
          items: payload.items
            ? payload.items.map(item => ({
                ...item,
                image: `https://image.tmdb.org/t/p/w185${item.poster_path}`,
              }))
            : [],
        }),
      ),
      ...handleAction(
        'setQuery',
        selectors.setQuery,
        (state, payload) => ({
          ...state,
          query: payload,
        }
