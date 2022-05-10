import selector from './selector';
import { getAll as getAllRooms } from '../../../../../redux/room/selector';
import { getId as getUserId } from '../../../../../redux/user/selector';
import { getId as getRoomId } from '../../../../../redux/room/selector';
import { getId as getIdUserInRoom } from '../../../../../redux/room/selector';
import { getId as getIdUserInRoomNotReady } from '../../../../../redux/room/selector';

const mapStateToProps = state => ({
  userId: getUserId(state),
  roomId: getRoomId(state),
  userIdInRoom: getIdUserInRoom(state),
  idUserInRoomNotReady: getIdUserInRoomNotReady(state),
  rooms: getAllRooms(state),
  ...selector(state),
});

const mapDispatchToProps = dispatch => ({
  onSetUserIdInRoom: userId => dispatch(setUser
