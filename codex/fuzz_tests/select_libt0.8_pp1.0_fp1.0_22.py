import select from '../../model/select';


const action = new createActions(_actions);

const REDUCER = 'client';
const FORM = `${REDUCER}Form`;
const MODAL = `${REDUCER}Modal`;

const _state = {
  loaded: false,
  loading: false,
  updating: false,
  form: {},
  data: [],
};

export const reducer = createReducer(_state, {
  [action.FORM.CLEAR]: (state) => {
    return {
      ...state,
      form: {},
    };
  },
  [action.MODAL.OPEN]: (state) => {
    return {
      ...state,
      modal: true,
    };
  },
  [action.MODAL.CLOSE]: (state) => {
    return {
      ...state,
      modal: false,
    };
  },
  [action.MODAL.TOGGLE]: (state) => {
    return {
      ...state,
      modal: !
