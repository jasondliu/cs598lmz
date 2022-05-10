import selectors from './selectors/selectorsContainer';

const mapStateToProps = state => ({
  selectors: selectors(state),
});

const mapDispatchToProps = dispatch =>
  bindActionCreators(
    {
      signout: logout,
    },
    dispatch,
  );

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Header);
