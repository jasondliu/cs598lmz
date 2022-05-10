import selectByPassword from '../../selectors/users';
import * as actions from '../../actions/users';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import FlatButton from 'material-ui/FlatButton';
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

// For custom `withStyles`


const customContentStyle = {
  width: '25%',
  maxWidth: 'none',
  paddingTop: '0px',
  marginTop: '-50px'
};

export class LoginPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      password: ''
    };
    this.setPassword = this.setPassword.bind(this);
  }

  setPassword(password) {
    this.set
