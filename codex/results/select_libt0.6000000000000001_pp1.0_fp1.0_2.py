import selector from './selector';
import { connect } from 'react-redux';

const mapStateToProps = state => {
  return {
    data: selector(state)
  }
}

const mapDispatchToProps = dispatch => {
  return {
    fetchData: () => dispatch(fetchData())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);
