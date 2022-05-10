import selectorLoginForm from "../../../LoginForm/LoginFormSelector";
import actionLoginForm from "../../../LoginForm/LoginFormAction";
import { connect } from "react-redux";
import styles from "./LoginPage.module.css";
import "./LoginPageMedia.css";

class LoginPage extends React.Component {
  checkUser = values => {
    if (!this.props.user.isLogin) {
      const { setLogin, showAlert } = this.props;
      setLogin(values);
      showAlert();
    }
  };

  initialValuesForm = () => ({
    email: "",
    password: ""
  });

  alert = () => {
    if (!this.props.user.isLogin) {
      return (
        <div className={styles.errorMessage}>
          The email or password is incorrect
        </div>
      );
    }
  };

  render() {
    const { user } = this.props;
    return (
      <div className={styles.wrapper}>
        <div
