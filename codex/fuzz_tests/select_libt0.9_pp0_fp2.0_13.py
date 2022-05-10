import selectors from './selectors';
import {bindActionCreators} from 'redux';
import * as actions from './actions';
import * as chatRoomActions from '../chatRoom/actions';
import * as chatActions from '../chat/actions';
import * as messageActions from '../message/actions';

function mapStateToProps(state, ownProps) {
  return {
    chatRoom: selectors.getChatRoom(state),
    loading: selectors.isLoading(state)
  };
}

function mapDispatchToProps(dispatch) {
  const dashboardActions = bindActionCreators(actions, dispatch);
  const chatRoomActions
