import selectors from './selectors';
import { getUser } from './actions';

const mapStateToProps = createStructuredSelector({
  user: selectors.getUser(),
  loading: selectors.getLoading(),
  error: selectors.getError(),
});

const mapDispatchToProps = dispatch => ({
  getUser: () => dispatch(getUser()),
});

const withConnect = connect(
  mapStateToProps,
  mapDispatchToProps,
);

export default compose(
  withConnect,
  memo,
)(User);
