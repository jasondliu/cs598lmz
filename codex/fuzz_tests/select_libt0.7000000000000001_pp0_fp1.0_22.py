import selectors from "./selectors";

const initialState = fromJS({
  dsFilter: {
    devices: [],
    conditions: []
  },
  dsFilterError: null,
  dsFilterLoading: false,
  dsFilterSaving: false
});

function dsFilterReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_DS_FILTER:
      return state
        .set("dsFilterLoading", true)
        .set("dsFilterError", null);
    case LOAD_DS_FILTER_SUCCESS:
      return state
        .set("dsFilterLoading", false)
        .set("dsFilter", fromJS(action.payload.dsFilter));
    case LOAD_DS_FILTER_ERROR:
      return state
        .set("dsFilterLoading", false)
        .set("dsFilterError", fromJS(action.payload.error));

    case ADD_DS_FILTER_CONDITION:
      return state.update("dsFilter", dsFilter =>
       
