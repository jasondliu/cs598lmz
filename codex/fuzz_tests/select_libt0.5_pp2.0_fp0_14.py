import selectors from '../../selectors';

const {
  createSelector,
} = selectors;

const getData = createSelector(
  (state) => state.data,
  (data) => data,
);

const getDataIsLoading = createSelector(
  (state) => state.data.isLoading,
  (isLoading) => isLoading,
);

const getDataIsLoaded = createSelector(
  (state) => state.data.isLoaded,
  (isLoaded) => isLoaded,
);

const getDataError = createSelector(
  (state) => state.data.error,
  (error) => error,
);

const getDataErrorMessage = createSelector(
  (state) => state.data.errorMessage,
  (errorMessage) => errorMessage,
);

const getDataIsValid = createSelector(
  (state) => state.data.isValid,
  (isValid) => isValid,
);

const getDataIsInvalid = createSelector(
  (state
