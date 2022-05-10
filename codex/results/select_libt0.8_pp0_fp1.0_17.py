import selector from '../selectors';

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated,
  authUser: selector(state.auth, 'user'),
  ...state.auth,
});

const mapDispatchToProps = dispatch => ({
  logout() {
    dispatch(logout())
  },
});

export default connect(mapStateToProps, mapDispatchToProps)(LoginContainer);
