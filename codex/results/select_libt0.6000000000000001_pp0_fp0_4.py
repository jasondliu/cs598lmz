import selector from './selector';

const mapStateToProps = (state) => ({
  currentUser: selector(state, 'currentUser'),
  isLoading: selector(state, 'isLoading'),
  hasError: selector(state, 'hasError'),
  errorMessage: selector(state, 'errorMessage'),
});

const mapDispatchToProps = (dispatch) => ({
  onSubmit: (payload) => dispatch(signup(payload)),
});

export default connect(mapStateToProps, mapDispatchToProps)(SignupForm);
