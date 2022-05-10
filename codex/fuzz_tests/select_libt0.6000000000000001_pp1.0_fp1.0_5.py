import selector from './selector';
import actionCreator from './actionCreator';
import { connect } from 'react-redux';

class App extends Component {
  componentDidMount() {
    this.props.getPosts();
  }
  render() {
    return (
      <div className="App">
        
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  posts: selector.getPosts(state),
  postsLoading: selector.getPostsLoading(state),
});

const mapDispatchToProps = (dispatch) => ({
  getPosts: () => dispatch(actionCreator.getPosts())
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(App);
