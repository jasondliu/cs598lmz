import selector from './selector'
import { connect } from 'react-redux'
import { ReduxState } from '../store'

import {
  getDashboard,
  changeSelectedTime,
} from '../actions'

import {
  TimeRange,
  TimeRangeId,
} from '../../interfaces'

interface DispatchProps {
  getDashboard: typeof getDashboard,
  changeSelectedTime: typeof changeSelectedTime,
}

interface OwnProps {
}

type Props = DispatchProps & OwnProps

const mapStateToProps = (state: ReduxState, ownProps: OwnProps) => {
  return selector(state, ownProps)
}

const mapDispatchToProps = (dispatch: any) => {
  return {
    getDashboard: () => {
      dispatch(getDashboard())
    },
    changeSelectedTime: (timeRangeId: TimeRangeId) => {
      dispatch(changeSelectedTime(timeRangeId))
    },
  }
}

const
