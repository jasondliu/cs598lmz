import selector from './selector';

const initialState = {
  entries: [],
  loading: false,
  error: null,
};

export const loadEntries = () => {
  return async (dispatch, getState, HttpClient) => {
    dispatch({ type: 'FETCH_ENTRIES' });
    try {
      const response = await HttpClient.get('/api/entries');
      dispatch({ type: 'FETCH_ENTRIES_SUCCESS', payload: response.data });
    } catch (err) {
      dispatch({ type: 'FETCH_ENTRIES_ERROR', payload: err.message });
    }
  };
};

export const createEntry = (entry) => {
  return async (dispatch, getState, HttpClient) => {
    dispatch({ type: 'CREATE_ENTRY' });
    try {
      const response = await HttpClient.post('/api/entries', entry);
      dispatch({ type: 'CREATE_ENTRY_SUCCESS', payload: response.data });
   
