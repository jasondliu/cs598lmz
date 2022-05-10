import selectors from './selectors'
import actions from './actions'

const mapStateToProps = (state) => {
  return {
    ...selectors(state),
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    ...actions(dispatch),
  }
}

const Container = connect(
  mapStateToProps,
  mapDispatchToProps
)(Component)

export default Container
