import selectUserAttribute from './selectUserAttribute';
import history from '../../router/history';
export const SET_DEFAULT_STATE = 'userAttribute/SET_DEFAULT_STATE';
export const LOAD_ITEM = 'userAttribute/LOAD_ITEM';
export const REMOVE_ITEM = 'userAttribute/REMOVE_ITEM';
export const CLEAR_ITEM = 'userAttribute/CLEAR_ITEM';
export const SET_ERRORS = 'userAttribute/SET_ERRORS';
export const SET_ISLOADING = 'userAttribute/SET_ISLOADING';


const initialState = {
  item: {},
  isLoading: false,
  isLoaded: false,
  errors: {},
};

export default (state = initialState, action) => {
  switch (action.type) {
    case SET_DEFAULT_STATE: {
      return { ...initialState };
    }
    case LOAD_ITEM:
      return {
        ...state,
        item: action.item,
        isLoaded: true,
      };

