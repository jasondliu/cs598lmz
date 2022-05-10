import selectors from './selectors';
import actions from './actions';
import get from 'lodash/get';
import { FORM_ERROR } from 'final-form';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { reduxForm } from 'redux-form';
import * as PropTypes from 'prop-types';

class SignupForm extends Component {
  static propTypes = {
    values: PropTypes.object,
    onSubmit: PropTypes.func,
    callError: PropTypes.any,
  };

  static defaultProps = {
    values: {},
    onSubmit: () => {},
    callError: null,
  };

  render() {
    const { values, handleSubmit, callError } = this.props;
    const error = get(callError, 'graphQLErrors');

    return (
      <form onSubmit={handleSubmit}>
        <H2>Sign Up</H2>
        <FlexBox>
          <Box>
            <Label htmlFor="email
