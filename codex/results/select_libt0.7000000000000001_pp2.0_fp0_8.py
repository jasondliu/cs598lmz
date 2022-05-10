import selectPicker from '../../../common/components/selectPicker';

const SelectPicker = selectPicker;

@Form.create({})
class FilterByForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      taskSelectList: [],
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    this.props.dispatch({
      type: 'taskTemplate/fetchTaskTree',
      payload: {
        pageNumber: 1,
        pageSize: 10,
      },
    });
  }

  componentWillReceiveProps(nextProps) {
    const { taskTemplate } = nextProps;
    const { treeList } = taskTemplate;
    this.setState({
      taskSelectList: treeList,
    });
  }

  handleSubmit() {
    const { form, onSearch } = this.props;
    form.validateFields((err, values) => {
      if (!err) {
