import selectors from './selectors';
import reducers from './reducers';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk';
import { getCookie } from './utilities/cookie';

// Get the Redux dev tools
const composeEnhancers =
    typeof window === "object" && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
        ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({})
        : compose;

const enhancer = composeEnhancers(applyMiddleware(thunk));

const store = createStore(reducers, enhancer);

class App extends Component {

    componentWillMount() {
        const { token, user } = getCookie();
        if (token && user) {
            store.dispatch({
                type: LOGIN_SUCCESS,
                payload: {
                    token,
                    user
                }
            });
        }
    }

    render
