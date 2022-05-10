import selectorUserData from './selectors/user-data';


const history = createBrowserHistory();

const middlewares = [
  thunk,
  routerMiddleware(history)
];
const composedEnhancers = compose(
  applyMiddleware(...middlewares),
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

const store = createStore(rootReducer, composedEnhancers);
initialStore(store);

const ConnectedRouter = connect(state => ({
  location: state.router.location
}))(Router);


function App() {
  return (
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/">
            <User>
              <Header />
              <div className="container">
                <Switch>
                  <Route path="/movies">
                    <Movies />
                  </Route
