import selectBills from './reducers/selectBills';
import selectAccounts from './reducers/selectAccounts';

// Actions
import { fetchBills } from './actions/fetchBills';
import { fetchAccounts } from './actions/fetchAccounts';

const store = createStore(
  combineReducers({
    selectBills,
    selectAccounts,
  }),
  applyMiddleware(thunk),
);

store.dispatch(fetchBills());
store.dispatch(fetchAccounts());

const Hellooo = () => (
  <Provider store={store}>
    <Router>
      <div>
        <Link to="/">Strona główna</Link> {' '}
        <Link to="/bills">Rachunki</Link> {' '}
        <Link to="/accounts">Konta</Link>
        <hr />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/bills" component={Bills}
