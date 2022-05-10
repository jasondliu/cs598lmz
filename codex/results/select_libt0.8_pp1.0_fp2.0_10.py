import selector from './selector';

class Login extends Component {
  state = {
    formData: {},
    error: '',
    isLoading: false,
    isSignUpLoading: false
  };

  componentDidMount() {
    this.props.dispatch(userInit());
  }

  componentDidUpdate(prevProps) {
    if (this.props.user.isAuthenticated) {
      this.props.dispatch(push('/'));
    }
  }

  handleSubmit = async e => {
    e.preventDefault();
    const { formData } = this.state;
    if (!formData.email) {
      this.setState({
        error: 'Email is required'
      });
      return;
    }
    if (!formData.password) {
      this.setState({
        error: 'Password is required'
      });
      return;
    }
    this.setState({ isLoading: true });

    this.props
      .dispatch(userLogin(formData))
      .catch
