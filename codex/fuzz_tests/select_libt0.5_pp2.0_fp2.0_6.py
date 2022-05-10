import selectors from './selectors';
import {
  getUser,
  getUserError,
  getUserLoading,
} from '../../../../redux/user/selectors';

const mapStateToProps = createStructuredSelector({
  user: getUser,
  userLoading: getUserLoading,
  userError: getUserError,
  ...selectors,
});

const mapDispatchToProps = {
  onGetUser: getUserAction,
};

const withConnect = connect(mapStateToProps, mapDispatchToProps);

export default compose(withConnect)(UserProfilePage);
