import select from 'select';

export default class TextareaAutosize extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: props.value,
      height: props.minHeight
    };
  }

  componentDidMount() {
    this.resize();
  }

  componentWillReceiveProps(nextProps) {
    if (this.state.value !== nextProps.value) {
      this.setState({
        value: nextProps.value
      });
    }
  }

  componentDidUpdate() {
    this.resize();
  }

  resize() {
    let {
      minRows,
      maxRows,
      style
    } = this.props;
    let {
      value
    } = this.state;
    let textarea = this.refs.textarea;
    let {
      height
    } = style;
    let minHeight = minRows * lineHeight + paddingSize;
    let maxHeight = maxRows * lineHeight
