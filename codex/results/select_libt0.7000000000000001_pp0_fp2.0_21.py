import selectedItemsReducer from "./selectedItemsReducer";
import cartReducer from "./cartReducer";

export default combineReducers({
  items: itemsReducer,
  selectedItems: selectedItemsReducer,
  cart: cartReducer,
});
