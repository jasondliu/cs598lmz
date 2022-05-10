import selector from '../selector';
import reducer from '../reducer';
import saga from '../saga';

const withConnect = connect(
  selector,
  {
  },
);

const withReducer = withRedux.reducer;
const withReducerAndSaga = withRedux(reducer, saga);

function mapStateToProps(state) {
  return {
    counterState: state.counter,
  };
}

export default compose(
  withReducerAndSaga,
  withConnect,
  withRouter,
)(Home);
