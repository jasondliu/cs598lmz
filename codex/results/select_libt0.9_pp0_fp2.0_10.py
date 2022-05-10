import selectedPosts from '../reducers/selectors';

class PostIndex extends React.Component {
  componentDidMount() {
    console.log(this.props);
    this.props.fetchPosts();
  }

  renderPosts() {
    const { posts } = this.props;
    if (this.props.posts.length > 0) {
      return <PostList posts={posts} />;
    }
    return null;
  }

  render() {
    return (
      <div>
        <h3>Posts</h3>
        <Link to="/posts/new" className="btn btn-primary">Add New Post</Link>
        {this.renderPosts()}
     </div>
    );
  }
}

const mapStateToProps = (state) => {
  return { posts: selectedPosts(state.posts) };
};

/*
function mapStateToProps(state) {
  return { posts: state.posts };
}
*/

export default connect(mapStateToProps, { fetchPosts
