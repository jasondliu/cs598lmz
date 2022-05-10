import select from '@appbaseio/reactivesearch/lib/components/utils/select';
import cx from 'classnames';

class TextField extends Component {
	constructor(props) {
		super(props);
		this.state = {
			currentValue: '',
		};
		this.type = 'match_phrase';
		this.locked = false;
		this.handleTextChange = this.handleTextChange.bind(this);
		this.withKeyboardShortcuts = this.withKeyboardShortcuts.bind(this);
	}

	componentWillMount() {
		this.previousQuery = null; // initial value for onQueryChange
	}

	componentDidMount() {
		const {
			defaultSelected,
			value,
			URLParams,
			componentId,
			filterLabel,
			customQuery,
			highlight,
			defaultQuery,
		} = this.props;

		this.setValue(
