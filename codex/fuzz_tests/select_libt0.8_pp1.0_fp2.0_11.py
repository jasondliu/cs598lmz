import selector from './selector';

const { getSettings, getNodes, getTerms } = selector;

export const fetchSettings = () => (dispatch, getState) => {
  const state = getState();
  const items = getSettings(state);
  if (items.length) {
    return;
  }
  dispatch(asyncAction({
    actionName: 'FETCH_SETTINGS',
    getPromise: wp.settings().get(),
  }));
};

export const fetchNodes = () => (dispatch, getState) => {
  const state = getState();
  const items = getNodes(state);
  if (items.length) {
    return;
  }
  dispatch(asyncAction({
    actionName: 'FETCH_NODES',
    getPromise: wp.nodes().get(),
  }));
};

export const fetchTerms = () => (dispatch, getState) => {
  const state = getState();
  const items = getTerms(state);
  if (
