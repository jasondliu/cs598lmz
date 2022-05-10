import selector from './selector'

const EXIT = 3000;

const defaultProps = {
  messages: [],
  messageDefault: {
    title: 'Иванов Иуда Иеронимович',
    text: 'Выполнено: Отчеты',
    type: 'success',
    icon: 'check',
    exit: EXIT
  },
  id: uniqid(),
  onDelete (id) {
    //
  },
  onDeleteAll (id) {
    //
  }
};

class Messages extends Component {

  componentDidMount () {
    document.addEventListener('click', this._onClickOutside, true);
  }

  componentDidUpdate (prevProps) {
    this._processImages();

    if (prevProps.messages.length < this.props.messages.length) {
      this._scrollToBottom();
    }
  }

  componentWillUnmount () {
    document
