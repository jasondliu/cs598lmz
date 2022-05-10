import selectedISODate from '../../../../../utils/selectedISODate';
import {
    setSectionComplete,
    setSectionInProgress
} from '../../../reducers/completionStatus';
import { change } from 'redux-form';

export class ReviewPage11 extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoading: false,
            isCompleted: false,
            isReviewing: false
        };
    }

    componentDidMount() {
        this.context.store.dispatch(setSectionComplete('ReviewPage11'));
        this.setState({
            isLoading: true
        });
        if (this.props.reviewStatus.confirm) {
            if (
                (this.props.formState.values.represents === 'self' &&
                    this.props.formState.values.militaryStatus === 'civilian') ||
                (this.props.formState.values.represents === 'someone else' &&
                    this.props.formState.values.military
