import selector from './selector';

const mapStateToProps = state => ({
  errorMessage: selector.errorMessage(state),
  successMessage: selector.successMessage(state),
});

export default connect(mapStateToProps)(Messages);
