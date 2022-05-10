import selectedMoviesReducer from "./selectedMoviesReducer";
import genreReducer from "./genreReducer";

export default combineReducers({
  movies: moviesReducer,
  selectedMovies: selectedMoviesReducer,
  genre: genreReducer
});
