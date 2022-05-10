import selector from './selector';

const mapDispatchToProps = {
  getAddress,
};

export default compose(
  connect(selector, mapDispatchToProps),
  withRouter,
)(GetAddress);
