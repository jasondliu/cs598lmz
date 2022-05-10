import selectCategory from '../actions';

const CategoryList = ({ categories, selectedCategory, onCategorySelect }) => {
  return (
    <ul className="category-list">
      {categories.map((category) => (
        <li key={category.id}>
          <button
            type="button"
            className="btn"
            style={{
              backgroundColor: selectedCategory === category.id ? '#f9f9f9' : 'white',
              fontWeight: selectedCategory === category.id ? 'bold' : 'normal',
            }}
            onClick={() => onCategorySelect(category)}
          >
            {category.name}
          </button>
        </li>
      ))}
    </ul>
  );
};

CategoryList.propTypes = {
  categories: PropTypes.array,
  selectedCategory: PropTypes.string,
  onCategorySelect: PropTypes.func,
};

const mapStateToProps = (state) => ({
   categories: state.categories,
   selectedCategory: state.selectedCategory,
});

