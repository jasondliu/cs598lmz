import selectedCards from '../utils/selectedCards';

const initialCardState = selectedCards;

const CLICK_CARD = 'CLICK_CARD';

export default function cardReducer(state = initialCardState, action) {
  switch(action.type) {
    case CLICK_CARD: {
      // action.index
      // change card at index
      let newCards = state.map(card => {
        if(card.index === action.index) {
          return Object.assign({}, card, {
            flipped : !card.flipped
          });
        }
        // return all the other cards
        return card;
      });
      return newCards;
    }
    default:
      return state;
  }
}
