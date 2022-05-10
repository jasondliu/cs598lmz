import selected from './selected'
import { createStore, applyMiddleware, combineReducers } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'

const reducer = combineReducers({
  products,
  selected
})

const store = createStore(reducer, composeWithDevTools(applyMiddleware(thunkMiddleware)))

export default store
export * from './products'
export * from './selected'
