import selector from './selector';

/**
 * @flow
 */

type Props = {
  saved: ?{
    parcel: ?Parcel,
    lot: ?Lot,
    zoning: ?Zoning,
    housing: ?Housing,
  },
  checkSaved: (ParcelKey) => void,
  showProfile: () => void,
  clearSaved: () => void,
  fetchMap: () => void,
  fetchDashboard: () => void,
  fetchForms: () => void,
  cookies: any,
};

class MainFeed extends React.Component<Props> {
  componentDidMount() {
    const { cookies } = this.props;
    api.get('auth/me').then((res) => {
      const { user } = res.data;
      cookies.set('uid', user.id, { path: '/' });
      cookies.set('username', user.username, { path: '/' });
      cookies.set('email', user.email, { path: '/' });
      this.props.fetch
