import selectors from '../../../redux/selectors';
import {
  fetchEventList,
  fetchEvent,
  clearEvent,
  createEvent,
  updateEvent,
  deleteEvent,
} from '../../../redux/actions/eventActions';
import EventList from './EventList';
import CreateEventForm from './CreateEventForm';
import UpdateEventForm from './UpdateEventForm';

class Event extends Component {
  static propTypes = {
    eventList: PropTypes.array.isRequired,
    event: PropTypes.object.isRequired,
    fetchEventList: PropTypes.func.isRequired,
    fetchEvent: PropTypes.func.isRequired,
    clearEvent: PropTypes.func.isRequired,
    createEvent: PropTypes.func.isRequired,
    updateEvent: PropTypes.func.isRequired,
    deleteEvent: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.fetchEventList();
  }

  componentWillUnmount() {
    this.props.clear
