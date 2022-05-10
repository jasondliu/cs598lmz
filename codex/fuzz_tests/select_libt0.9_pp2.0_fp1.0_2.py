import selector from './selector'

const List = ({ fetchPosts, posts = [] }) => {
  useEffect(() => {
    fetchPosts()
  }, [fetchPosts])

  return <PostList posts={posts} />
}

List.propTypes = {
  fetchPosts: PropTypes.func.isRequired,
  posts: PropTypes.array
}

const mapStateToProps = state => ({
  posts: selector(state, 'posts')
})

export default connect(
  mapStateToProps,
  { fetchPosts }
)(List)
