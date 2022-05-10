import selectors from './map/selectors';
import type { State, InjectProps } from './types';


const RECONNECT_INTERVAL_MS = 1000;

export default class Connection extends React.Component<Props, State> {

  static contextTypes = {
    locale: PropTypes.string,
    localize: PropTypes.func,
  };

  static defaultProps = {
    onConnection: noop,
    onDisconnect: noop,
  }

  state: State = {
    isConnecting: false,
    isConnected: false,
    onConnection: noop,
  }

  connectedCountdown: ?IntervalID = null;
  connectionTimer: ?IntervalID = null;

  componentDidMount() {
    const { socket } = this.props;

    const open = () => {
      const { isConnected, isConnecting } = this.state;

      if (!isConnected && !isConnecting) {
        this.setState({
          isConnected: true,
          isConnecting: true,
       
