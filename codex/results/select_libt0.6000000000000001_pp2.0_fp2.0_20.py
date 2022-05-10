import selected from '../images/selected.png'
import unselected from '../images/unselected.png'
import close from '../images/close.png'
import { getUser, getToken, setUser, setToken, removeUser, removeToken } from '../utils/auth'
import { Toast } from 'antd-mobile'
import { withRouter } from 'react-router-dom'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import * as actions from '../actions/user'
import * as shopActions from '../actions/shop'

class Mine extends Component {
  constructor(props) {
    super(props)
    this.state = {
      user: getUser(),
      token: getToken(),
      open: false
    }
  }
  componentDidMount() {
    this.props.userActions.getUserInfo({
      user_id: this.state.user
    })
    this.props.shopActions.getShopInfo({
      shop_id: this.
