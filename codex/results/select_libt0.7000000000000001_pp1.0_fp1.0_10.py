import select from 'select';
import App from './components/App';

import { getNotes, addNote, removeNote, updateNote, getNote } from './actions/notes';
import { getTags } from './actions/tags';

import { getNotesState, getTagsState } from './reducers';

import { init } from './utils/db';
import { getDb, getAllData } from './utils/db';

import { parseTags } from './utils/parser';

const store = createStore(reducer, applyMiddleware(thunk));

getDb();

init();

// addNote({
// 	title: 'My first note',
// 	content: '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus condimentum, nisl sed tincidunt ullamcorper, mi augue elementum lorem, id accumsan nulla orci et nisl. Sed placerat, odio vitae porttitor sagittis, velit lectus volutpat
