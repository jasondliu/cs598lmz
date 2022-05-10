import selections from "./Selections";
import { InitData, InitMacro, AddMacroItem } from "../actions/macro";
import { MACRO_PROPERTY } from "../constants/macro";

const logger = createLogger();

const sagaMiddleware = createSagaMiddleware();

const middlewares = [thunkMiddleware, sagaMiddleware, logger];

const createStoreWithMiddleware = compose(applyMiddleware(...middlewares))(
  createStore
);

const rootReducer = combineReducers({ active, prevActive, selections });

const store = createStoreWithMiddleware(rootReducer);

const persistedState = loadState();
if (persistedState) {
  if (persistedState.active) {
    store.dispatch(InitData(persistedState.active));
  }

  if (persistedState.prevActive) {
    store.dispatch(InitMacro(persistedState.prevActive));
  }

  if (persistedState.selections) {
    store.dispatch(AddMacroItem(MAC
