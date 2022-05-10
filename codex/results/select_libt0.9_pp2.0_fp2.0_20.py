import selector from './selector';
import { Provider } from 'react-redux';
import store from './store';
import { update, execute } from './actions';

function run() {
  ReactDOM.render(
    <Provider store={store}>
      {selector}
    </Provider>,
    document.getElementById('app')
  );
}

window.onload = () => {
  setTimeout(() => {
    run()
  }, 0);
};

// This is necessary to in case of HMR, 
// since the main module is replaced, but the onload event is not triggered.
if (module.hot) {
  module.hot.accept();
  module.hot.dispose(run);
}

document.addEventListener('keydown', ({ keyCode }) => {
  if (keyCode === 13) {
    // 13 is the ENTER key
    const state = store.getState();
    const { code, env } = state;
    store.dispatch(execute(code, env));
  }
});
