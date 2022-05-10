import selector from './selector';
import './style.scss';

const { getCategories } = selector;

const Categories = ({ categories }) => (
  <div className='categories'>
    {categories.map(category => (
      <div key={category.name} className='category'>
        <h2 className='category-title'>{category.name}</h2>
        <div className='category-items'>
          {category.items.map(item => (
            <div key={item.name} className='category-item'>
              <div className='category-item-left'>
                <div className='category-item-name'>{item.name}</div>
                <div className='category-item-description'>{item.description}</div>
              </div>
              <div className='category-item-right'>
                {item.price}
              </div>
            </div>
          ))}
        </div>
      </div>
    ))}
  </div>
);

Categories.propTypes
