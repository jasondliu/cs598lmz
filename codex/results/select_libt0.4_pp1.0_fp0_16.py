import selectors from './selectors';
import { createReducer } from '../../../utils/reducers';

const initialState = {
  isLoading: false,
  isEditing: false,
  error: {},
  data: {},
};

export default createReducer({
  [actions.getUserRequest]: state => ({
    ...state,
    isLoading: true,
    error: {},
  }),
  [actions.getUserSuccess]: (state, { payload }) => ({
    ...state,
    data: payload,
    isLoading: false,
  }),
  [actions.getUserFailure]: (state, { payload }) => ({
    ...state,
    error: payload,
    isLoading: false,
  }),
  [actions.editUserRequest]: state => ({
    ...state,
    isEditing: true,
    error: {},
  }),
  [actions.editUserSuccess]: (state, { payload }) => ({
    ...state,
    data: payload,
    isEditing: false,
  }
